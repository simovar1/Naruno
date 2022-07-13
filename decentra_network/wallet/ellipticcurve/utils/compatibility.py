#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2021 Decentra Network Developers
Copyright (c) 2018 Stark Bank S.A.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from sys import version_info as pyVersion
from binascii import hexlify, unhexlify


if pyVersion.major == 3:
    # py3 constants and conversion functions

    stringTypes = (str,)
    intTypes = (int, float)

    def toString(string, encoding="utf-8"):
        return string.decode(encoding)

    def toBytes(string, encoding="utf-8"):
        return string.encode(encoding)

    def safeBinaryFromHex(hexadecimal):
        if len(hexadecimal) % 2 == 1:
            hexadecimal = f"0{hexadecimal}"
        return unhexlify(hexadecimal)

    def safeHexFromBinary(byteString):
        return toString(hexlify(byteString))

else:
    # py2 constants and conversion functions

    stringTypes = (str, unicode)
    intTypes = (int, float, long)

    def toString(string, encoding="utf-8"):
        return string

    def toBytes(string, encoding="utf-8"):
        return string

    def safeBinaryFromHex(hexadecimal):
        return unhexlify(hexadecimal)

    def safeHexFromBinary(byteString):
        return hexlify(byteString)