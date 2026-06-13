#!/usr/bin/env python3
"""
BMS Archive — Local Admin Server
Run: python3 admin_server.py
Then open: http://localhost:5050
"""
import http.server, json, os, webbrowser, threading

BASE   = os.path.dirname(os.path.abspath(__file__))
DATA   = os.path.join(BASE, 'data.json')
HTML   = os.path.join(BASE, 'admin.html')
PORT   = 5050

REQUIRED = ['scientific_name', 'common_name', 'type', 'article_count']

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ('/', '/admin', '/admin.html'):
            self._serve_file(HTML, 'text/html; charset=utf-8')
        elif self.path == '/api/data':
            with open(DATA, 'rb') as f:
                body = f.read()
            self._respond(200, 'application/json', body)
        else:
            self._respond(404, 'text/plain', b'Not found')

    def do_POST(self):
        if self.path == '/api/data':
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length)
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError as e:
                return self._respond(400, 'application/json',
                                     json.dumps({'error': f'Ugyldig JSON: {e}'}).encode())

            # Server-side validation
            errors = []
            for i, entry in enumerate(payload):
                name = entry.get('scientific_name') or f'Post #{i+1}'
                for field in REQUIRED:
                    if not entry.get(field):
                        errors.append(f'{name}: mangler "{field}"')
                if entry.get('type') not in ('Fungi', 'Plant'):
                    errors.append(f'{name}: type skal være "Fungi" eller "Plant"')
                if not isinstance(entry.get('primary_categories'), list):
                    errors.append(f'{name}: primary_categories skal være et array')
                src = entry.get('sources', {})
                if not isinstance(src.get('top_studies_urls'), list):
                    errors.append(f'{name}: sources.top_studies_urls skal være et array')

            if errors:
                return self._respond(422, 'application/json',
                                     json.dumps({'errors': errors}).encode())

            with open(DATA, 'w', encoding='utf-8') as f:
                json.dump(payload, f, indent=2, ensure_ascii=False)

            self._respond(200, 'application/json', json.dumps({'ok': True, 'count': len(payload)}).encode())
        else:
            self._respond(404, 'text/plain', b'Not found')

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def _respond(self, status, ctype, body):
        self.send_response(status)
        self.send_header('Content-Type', ctype)
        self.send_header('Content-Length', str(len(body)))
        self._cors()
        self.end_headers()
        self.wfile.write(body)

    def _serve_file(self, path, ctype):
        with open(path, 'rb') as f:
            body = f.read()
        self._respond(200, ctype, body)

    def log_message(self, fmt, *args):
        print(f'  {self.address_string()} {fmt % args}')

if __name__ == '__main__':
    server = http.server.HTTPServer(('127.0.0.1', PORT), Handler)
    url = f'http://localhost:{PORT}'
    print(f'\n  BMS Admin Panel → {url}')
    print('  Stop med Ctrl+C\n')
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n  Server stoppet.')
