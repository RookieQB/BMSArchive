## Summary

<!-- What does this PR do? 1–3 bullet points. -->

- 

## Type of change

- [ ] New monograph (species: _______)
- [ ] Monograph update (species: _______)
- [ ] Bug fix
- [ ] Infrastructure / deployment change
- [ ] Documentation
- [ ] Other: _______

## Scientific QA

<!-- Required for any data.json changes. -->

- [ ] All new claims have verifiable PubMed sources
- [ ] Evidence language matches evidence level (A–U scale)
- [ ] No animal/in vitro evidence presented as human efficacy
- [ ] No disease treatment/cure/prevention claims
- [ ] No unqualified "safe" claims
- [ ] Safety fields (pregnancy, lactation, drug interactions) complete and conservative

## Checklist

- [ ] `python3 scripts/validate_archive_data.py` passes with 0 errors
- [ ] No secrets or API keys in committed files
- [ ] Admin tools NOT included in deploy files
- [ ] CI passing

## For new monographs: pre-publish gate

Run `/workflow:pre-publish [species]` and paste the result:

```
[paste pre-publish report here]
```

## Notes

<!-- Anything the reviewer needs to know. Known limitations, deferred issues, etc. -->
