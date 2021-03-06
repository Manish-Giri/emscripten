#!/usr/bin/env python3

'''
This is a helper tool which is designed to make it possible
for other apps to read emscripten's configuration variables
in a unified way.  Usage:

  em-config VAR_NAME

This tool prints the value of the variable to stdout if one
is found, or exits with 1 if the variable does not exist.
'''

from __future__ import print_function
import sys
import re
from tools import shared

if len(sys.argv) != 2 or \
  not re.match(r"^[\w\W_][\w\W_\d]*$", sys.argv[1]) or \
  not (sys.argv[1] in dir(shared)):
  print('Usage: em-config VAR_NAME', file=sys.stderr)
  exit(1)

print(getattr(shared, sys.argv[1]))
