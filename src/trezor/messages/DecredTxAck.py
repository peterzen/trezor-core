# Automatically generated by pb2py
import protobuf as p
from .DecredTransactionType import DecredTransactionType


class DecredTxAck(p.MessageType):
    FIELDS = {
        1: ('tx', DecredTransactionType, 0),
    }
    MESSAGE_WIRE_TYPE = 121
