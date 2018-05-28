from ctypes import *
import struct

class TCP(Structure):
    _fields_=[
        ("src", c_ushort),
        ("dst", c_ushort),
        ("seqq", c_long),
        ("ack", c_long),
        ("off", c_ubyte, 4),
        ("res", c_ubyte, 4),
        ("flag",  c_ubyte),
        ("win", c_ushort),
        ("check", c_ushort),
        ("urg", c_ushort),
        ]