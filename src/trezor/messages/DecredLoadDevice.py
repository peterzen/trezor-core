# Automatically generated by pb2py
import protobuf as p
from .HDNodeType import HDNodeType


class DecredLoadDevice(p.MessageType):
    FIELDS = {
        1: ('mnemonic', p.UnicodeType, 0),
        2: ('node', HDNodeType, 0),
        3: ('pin', p.UnicodeType, 0),
        4: ('passphrase_protection', p.BoolType, 0),
        5: ('language', p.UnicodeType, 0),  # default='english'
        6: ('label', p.UnicodeType, 0),
        7: ('u2f_counter', p.UVarintType, 0),
    }
    MESSAGE_WIRE_TYPE = 114
