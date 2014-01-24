#!/usr/bin/env python

import sys
import chardet

data = sys.stdin.read()
encoding = chardet.detect( data )[ "encoding" ]

print data.decode( encoding ).encode( sys.getfilesystemencoding() ),
