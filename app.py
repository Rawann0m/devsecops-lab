from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        content = """
<html>
<head>
    <title>DevSecOps Lab</title>
</head>
<body style="background-color:#111; color:white; text-align:center; font-family:Arial;">
    <h1>DevSecOps Lab </h1>
    <p>Running Successfully.</p>
    <p>Local Development Environment Working.</p>
</body>
</html>
"""

        self.wfile.write(content.encode())

server = HTTPServer(("", PORT), MyHandler)
print(f"Server running on http://localhost:{PORT}")
server.serve_forever()