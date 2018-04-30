#!/usr/bin/env python3
'''
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
'''
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer


class Server(BaseHTTPRequestHandler):
    def set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        path = str(self.path)
        headers = str(self.headers)
        logging.info("GET request, \nPath: {}\nHeaders:\n{}\n".format(path, headers))
        self.set_response()
        self.wfile.write("GET request for {}\n".format(self.path).encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])  # <--- Gets the size of data
        path = str(self.path)
        headers = str(self.headers)
        data = self.rfile.read(content_length).decode("utf-8")  # <--- Gets the data itself
        logging.info("POST request,\nPath: {}\nHeaders:\n{}\nBody:\n{}\n".format(path, headers, data))
        self.set_response()
        self.wfile.write("POST request for {}\n".format(self.path).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=Server, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    logging.info("Starting httpd...\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info("Stopping httpd...\n")


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
