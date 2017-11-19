from trezor.wire import register, protobuf_workflow
from trezor.utils import unimport
from trezor.messages.wire_types import \
    DecredGetAddress


@unimport
def dispatch_DecredGetAddress(*args, **kwargs):
    from .decred_get_address import decred_get_address
    return decred_get_address(*args, **kwargs)


def boot():
    register(DecredGetAddress, protobuf_workflow, dispatch_DecredGetAddress)
