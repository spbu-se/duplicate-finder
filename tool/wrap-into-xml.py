#!/usr/bin/env python

import re
import sys

def esc(s):
  """Minimal XML escape"""
  return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

re_nt = re.compile("\n[\t ]+", re.MULTILINE)
re_lf = re.compile("\n\n(\n)+", re.MULTILINE)

def strip(s):
  crlfr = s.replace("\r\n", "\n").replace("\r", "\n")
  crlfr = re_nt.sub("\n", crlfr)
  crlfr = re_lf.sub("\n\n", crlfr)
  return crlfr

plaintext = sys.stdin.buffer.read().decode('utf8')

escaped = esc(strip(plaintext))
wrapped = "<?xml version=\"1.0\" encoding=\"utf-8\" ?>\n<plainxml>" + escaped + "\n</plainxml>"

sys.stdout.buffer.write(wrapped.encode('utf8'))
