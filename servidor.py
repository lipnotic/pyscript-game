from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

PORTA = 8000

class COIRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Resource-Policy', 'cross-origin')
        super().end_headers()

if __name__ == '__main__':
    servidor = ThreadingHTTPServer(('127.0.0.1', PORTA), COIRequestHandler)
    print(f'Jogo disponivel em http://localhost:{PORTA}')
    print('Pressione Ctrl+C para encerrar.')
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        servidor.server_close()
