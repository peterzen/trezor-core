# Automatically generated by pb2py
import protobuf as p


class DecredGetAddress(p.MessageType):
    FIELDS = {
        1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        2: ('show_display', p.BoolType, 0),
    }
    MESSAGE_WIRE_TYPE = 115
