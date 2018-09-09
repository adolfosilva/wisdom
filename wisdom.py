#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from random import randint

def random_line(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        return lines[randint(0, len(lines) - 1)]

class random_wisdom(BaseHTTPRequestHandler):
  def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes(random_line(sys.argv[2]), "utf8"))
        return

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: {} PORT FILE'.format(sys.argv[0]))
        sys.exit(1)
    addr = ('0.0.0.0', int(sys.argv[1]))
    print('Starting server on {}:{}'.format(addr[0], addr[1]))
    server = HTTPServer(addr, random_wisdom)
    print('Awaiting connections...')
    server.serve_forever()
