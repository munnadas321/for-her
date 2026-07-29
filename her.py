from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import webbrowser


def run_server(port: int = 8000):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    target_file = 'love.html' if os.path.exists(os.path.join(base_dir, 'love.html')) else 'sorry_baby.html'

    class QuietHandler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=base_dir, **kwargs)

    webbrowser.open(f'http://127.0.0.1:{port}/{target_file}')

    server = HTTPServer(('127.0.0.1', port), QuietHandler)
    print(f'Server running at http://127.0.0.1:{port}/{target_file}')
    print('Press Ctrl+C to stop')
    server.serve_forever()


if __name__ == '__main__':
    run_server()
