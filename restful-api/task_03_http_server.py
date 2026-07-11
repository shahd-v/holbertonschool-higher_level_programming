#!/usr/bin/python3
"""Provide a small REST-style API using Python's http.server module."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handle GET requests for a small demonstration API."""

    def _send_text_response(self, status_code, body):
        """Send a plain text HTTP response."""
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def _send_json_response(self, status_code, data):
        """Send a JSON HTTP response."""
        response = json.dumps(data).encode("utf-8")

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self):
        """Route GET requests to the available API endpoints."""
        if self.path == "/":
            self._send_text_response(
                200,
                "Hello, this is a simple API!"
            )
        elif self.path == "/data":
            self._send_json_response(
                200,
                {"name": "John", "age": 30, "city": "New York"}
            )
        elif self.path == "/status":
            self._send_text_response(200, "OK")
        elif self.path == "/info":
            self._send_json_response(
                200,
                {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                }
            )
        else:
            self._send_text_response(404, "Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Start the HTTP server on port 8000."""
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
