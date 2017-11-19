from trezor import wire, ui
from trezor.utils import unimport


@unimport
async def decred_get_address(ctx, msg):
    from trezor.messages.DecredAddress import DecredAddress
    from trezor.messages.FailureType import ProcessError
    from ..common import coins
    from ..common import seed

    address_n = msg.address_n or ()
    coin_name = msg.coin_name or 'Decred'

    node = await seed.get_root(ctx)
    node.derive_path(address_n)
    coin = coins.by_name(coin_name)
    address = node.decred_address(coin.address_type)

    if msg.show_display:
        await _show_address(ctx, address)

    return DecredAddress(address=address)


async def _show_address(ctx, address):
    from trezor.messages.ButtonRequestType import Address
    from trezor.ui.text import Text
    from trezor.ui.qr import Qr
    from trezor.ui.container import Container
    from ..common.confirm import require_confirm

    lines = _split_address(address)
    content = Container(
        Qr(address, (120, 135), 3),
        Text('Confirm address', ui.ICON_RESET, ui.MONO, *lines))
    await require_confirm(ctx, content, code=Address)


def _split_address(address):
    from trezor.utils import chunks
    return chunks(address, 17)
