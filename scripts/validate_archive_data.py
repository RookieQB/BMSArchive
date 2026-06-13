#!/usr/bin/env python3
"""
BMS Archive — Data Validation Script
Validates data.json for required fields, safety sections, citation format,
placeholder text, and data integrity.

Usage:
    python3 scripts/validate_archive_data.py
    python3 scripts/validate_archive_data.py --strict
    python3 scripts/validate_archive_data.py --entry "Ganoderma lucidum"

Exit codes:
    0 = no errors (warnings may exist)
    1 = one or more errors found
"""

import json
import sys
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_FILE = ROOT / "data.json"

ERRORS = []
WARNINGS = []

# ── Helpers ──────────────────────────────────────────────────────────────────

def error(entry_name, field, message):
    ERRORS.append(f"[ERROR] {entry_name} | {field} | {message}")

def warn(entry_name, field, message):
    WARNINGS.append(f"[WARN]  {entry_name} | {field} | {message}")

def field_empty(value):
    if value is None:
        return True
    if isinstance(value, str) and value.strip() == "":
        return True
    if isinstance(value, list) and len(value) == 0:
        return True
    return False

def contains_placeholder(text):
    if not isinstance(text, str):
        return False
    text_lower = text.lower()
    placeholders = [
        "todo", "fixme", "lorem ipsum", "insert source", "citation needed",
        "tbd", "placeholder", "add here", "fill in", "to be completed",
        "[source]", "[citation]", "[pmid]", "[reference]",
    ]
    return any(p in text_lower for p in placeholders)

def contains_unqualified_safe(text):
    """Detect 'safe' without qualifying words like 'insufficient', 'limited', 'not'."""
    if not isinstance(text, str):
        return False
    text_lower = text.lower()
    if "safe" not in text_lower:
        return False
    qualifying_words = [
        "insufficient", "limited", "not safe", "unsafe", "not established",
        "not recommended", "unknown", "may not be", "cannot", "caution",
        "inadequate", "no data", "no safety data", "limited safety", "uncertain"
    ]
    for q in qualifying_words:
        if q in text_lower:
            return False
    return True

def pubmed_url_valid(url):
    return isinstance(url, str) and "pubmed.ncbi.nlm.nih.gov" in url and url.startswith("https://")

def contains_instagram_social(text):
    """Flag any Instagram or social media content in archive data."""
    if not isinstance(text, str):
        return False
    social_terms = ["instagram", "tiktok", "facebook", "@thebms", "reel", "caption",
                    "influencer", "social media post", "follow us"]
    text_lower = text.lower()
    return any(t in text_lower for t in social_terms)

# ── Per-entry validation ──────────────────────────────────────────────────────

def validate_entry(entry, index, strict=False):
    name = entry.get("scientific_name") or f"Entry #{index}"

    # ── Top-level required fields ──────────────────────────────────────────
    for field in ["scientific_name", "common_name", "type", "article_count", "primary_categories"]:
        if field_empty(entry.get(field)):
            error(name, field, f"Required field is missing or empty")

    # ── type must be exactly Fungi or Plant ───────────────────────────────
    if entry.get("type") not in ("Fungi", "Plant"):
        error(name, "type", f"Must be 'Fungi' or 'Plant', got: {repr(entry.get('type'))}")

    # ── article_count must be an integer ─────────────────────────────────
    if not isinstance(entry.get("article_count"), int):
        error(name, "article_count", "Must be an integer")

    # ── sources ───────────────────────────────────────────────────────────
    sources = entry.get("sources", {})
    if not isinstance(sources, dict):
        error(name, "sources", "Must be an object")
    else:
        urls = sources.get("top_studies_urls", [])
        if field_empty(urls):
            error(name, "sources.top_studies_urls", "No PubMed URLs provided")
        else:
            for i, url in enumerate(urls):
                if not pubmed_url_valid(url):
                    error(name, f"sources.top_studies_urls[{i}]",
                          f"Not a valid PubMed URL: {url!r}")

    # ── narrative_summary ─────────────────────────────────────────────────
    ns = entry.get("narrative_summary", {})
    if not isinstance(ns, dict):
        error(name, "narrative_summary", "Must be an object")
    else:
        for field in ["historical_use", "modern_application", "side_effects", "contraindications"]:
            val = ns.get(field)
            if field_empty(val):
                error(name, f"narrative_summary.{field}", "Empty — required")
            else:
                if contains_placeholder(val):
                    error(name, f"narrative_summary.{field}", "Contains placeholder text")
                if contains_instagram_social(val):
                    error(name, f"narrative_summary.{field}",
                          "Contains Instagram/social media content — not allowed in archive data")
                if field in ("side_effects", "contraindications") and contains_unqualified_safe(val):
                    warn(name, f"narrative_summary.{field}",
                         "Contains unqualified 'safe' claim — verify this is evidence-based")

    # ── clinical_data ─────────────────────────────────────────────────────
    cd = entry.get("clinical_data", {})
    if not isinstance(cd, dict):
        error(name, "clinical_data", "Must be an object")
        return

    # used_part
    if field_empty(cd.get("used_part")):
        error(name, "clinical_data.used_part", "Empty — required")

    # primary_active_compounds
    if field_empty(cd.get("primary_active_compounds")):
        warn(name, "clinical_data.primary_active_compounds", "Empty — recommended")

    # mechanism_of_action
    if field_empty(cd.get("mechanism_of_action")):
        error(name, "clinical_data.mechanism_of_action", "Empty — required")
    elif contains_placeholder(cd.get("mechanism_of_action", "")):
        error(name, "clinical_data.mechanism_of_action", "Contains placeholder text")

    # pharmacokinetics (all four ADME fields required)
    pk = cd.get("pharmacokinetics", {})
    if not isinstance(pk, dict):
        error(name, "clinical_data.pharmacokinetics", "Must be an object")
    else:
        for field in ["absorption", "distribution", "metabolism", "excretion"]:
            if field_empty(pk.get(field)):
                error(name, f"clinical_data.pharmacokinetics.{field}", "Empty — required")
            elif contains_placeholder(pk.get(field, "")):
                error(name, f"clinical_data.pharmacokinetics.{field}", "Contains placeholder text")

    # safety_and_interactions
    safety = cd.get("safety_and_interactions", {})
    if not isinstance(safety, dict):
        error(name, "clinical_data.safety_and_interactions", "Must be an object")
    else:
        if field_empty(safety.get("drug_interactions")):
            error(name, "clinical_data.safety_and_interactions.drug_interactions",
                  "Empty — required (write 'No clinically significant interactions established' if none documented, with rationale)")
        if field_empty(safety.get("toxicity")):
            error(name, "clinical_data.safety_and_interactions.toxicity",
                  "Empty — required (write 'No toxicity data available' if not documented)")
        if contains_unqualified_safe(safety.get("drug_interactions", "")) or \
           contains_unqualified_safe(safety.get("toxicity", "")):
            warn(name, "clinical_data.safety_and_interactions",
                 "Contains unqualified 'safe' claim — verify evidence basis")

    # special_precautions (all four sections required)
    prec = cd.get("special_precautions", {})
    if not isinstance(prec, dict):
        error(name, "clinical_data.special_precautions", "Must be an object")
    else:
        for field in ["pregnancy", "lactation", "hepatic_impairment", "renal_impairment"]:
            val = prec.get(field)
            if field_empty(val):
                error(name, f"clinical_data.special_precautions.{field}",
                      "Empty — required (write 'Insufficient data' if not documented, not a blank field)")
            else:
                if contains_placeholder(val):
                    error(name, f"clinical_data.special_precautions.{field}",
                          "Contains placeholder text")
                if contains_unqualified_safe(val):
                    warn(name, f"clinical_data.special_precautions.{field}",
                         "Contains unqualified 'safe' claim — pregnancy/lactation require explicit evidence basis")

    # ── Strict mode: additional checks ───────────────────────────────────
    if strict:
        # Check mechanism of action uses <strong> tags for at least one target
        moa = cd.get("mechanism_of_action", "")
        if moa and "<strong>" not in moa:
            warn(name, "clinical_data.mechanism_of_action",
                 "[strict] No <strong> tags found — key pharmacological targets should be highlighted")

        # Check primary_categories has at least one meaningful entry
        cats = entry.get("primary_categories", [])
        if isinstance(cats, list) and len(cats) < 1:
            warn(name, "primary_categories", "[strict] No categories defined")

# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="BMS Archive data.json validator")
    parser.add_argument("--strict", action="store_true",
                        help="Enable additional style/convention checks")
    parser.add_argument("--entry", type=str, default=None,
                        help="Validate only entries matching this name")
    args = parser.parse_args()

    print(f"\nBMS Archive — Data Validation")
    print(f"File: {DATA_FILE}")
    print(f"Mode: {'strict' if args.strict else 'standard'}")
    if args.entry:
        print(f"Filter: {args.entry}")
    print("─" * 60)

    # Step 1: JSON parse
    try:
        with open(DATA_FILE, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"\n[FATAL] JSON parse error — fix this before anything else:")
        print(f"  Line {e.lineno}, Col {e.colno}: {e.msg}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"\n[FATAL] data.json not found at {DATA_FILE}")
        sys.exit(1)

    # Step 2: Basic counts
    fungi = [d for d in data if d.get("type") == "Fungi"]
    plants = [d for d in data if d.get("type") == "Plant"]
    other = [d for d in data if d.get("type") not in ("Fungi", "Plant")]

    print(f"\nEntries: {len(data)} total ({len(fungi)} Fungi, {len(plants)} Plant"
          + (f", {len(other)} invalid type" if other else "") + ")")

    # Step 3: Validate each entry
    for i, entry in enumerate(data):
        name = entry.get("scientific_name") or f"Entry #{i}"
        if args.entry and args.entry.lower() not in name.lower():
            continue
        validate_entry(entry, i, strict=args.strict)

    # Step 4: Report
    print()
    if ERRORS:
        print(f"ERRORS ({len(ERRORS)}):")
        for e in ERRORS:
            print(f"  {e}")
        print()

    if WARNINGS:
        print(f"WARNINGS ({len(WARNINGS)}):")
        for w in WARNINGS:
            print(f"  {w}")
        print()

    # Summary
    if not ERRORS and not WARNINGS:
        print("✓ All checks passed — no errors or warnings.")
    elif not ERRORS:
        print(f"✓ No errors. {len(WARNINGS)} warning(s) — review recommended.")
    else:
        print(f"✗ {len(ERRORS)} error(s) found. Fix before committing or deploying.")

    print()

    sys.exit(1 if ERRORS else 0)


if __name__ == "__main__":
    main()
