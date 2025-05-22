import http.server
import socketserver

class HealthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/_ah/health":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Healthy")
            
    def log_message(self, format, *args):
        # Suppress log messages
        return

def start_health_server():
    """Start a health check server on port 8081"""
    import threading
    
    def run_server():
        with socketserver.TCPServer(("", 8081), HealthHandler) as httpd:
            httpd.serve_forever()
    
    t = threading.Thread(target=run_server, daemon=True)
    t.start()
    return t