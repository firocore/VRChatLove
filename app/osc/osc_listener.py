import asyncio

from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
from app.osc.osc_store import OSCParameterStore

store = OSCParameterStore()


debug_widget = None  # глобальная переменная

def set_debug_widget(widget):
    global debug_widget
    debug_widget = widget

def osc_handler(address: str, *args):
    value = args[0] if args else None
    # print(f"OSC param: {address} = {value}")

    if address == "/avatar/change":
        debug_widget.clear_params.emit()
        store.clear_all()
        return
    
    address = address.replace("/avatar/parameters/", "")
    
    store.update(address, value)

    if debug_widget is not None:
        debug_widget.param_updated.emit(address, value)

dispatcher = Dispatcher()
dispatcher.set_default_handler(osc_handler)

async def start_osc_server(ip="0.0.0.0", port=9001):
    server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()
    print(f"OSC server listening on {ip}:{port}")
    return transport, protocol
