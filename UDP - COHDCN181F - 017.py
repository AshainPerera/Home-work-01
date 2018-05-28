from ctypes import *
import struct

class UDP(Structure):
    _fields_=[
        ("src", c_ushort),
        ("dst", c_ushort),
        ("len", c_short),
        ("check", c_short),
        ]