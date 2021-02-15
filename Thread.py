import asyncio
import sys
import threading
from aioudp import UDPServer
from Server import MyUDPServer


class UDPServerThread(threading.Thread):
    loop = None
    server_address = None
    server_port = None
    args = None

    def __init__(self, server_address_, server_port_, args):
        if args is not None:
            self.args = args
        self.setup_loop_policy()
        self.server_address = server_address_
        self.server_port = server_port_
        self.loop = asyncio.new_event_loop()
        super(UDPServerThread, self).__init__()
        self.server = self.main(self.loop, self.server_address, self.server_port)

    @staticmethod
    def setup_loop_policy():
        if sys.platform == 'win32':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    @staticmethod
    async def main(loop_method, server_address_, server_port_):
        udp = UDPServer()
        udp.run(server_address_, server_port_, loop=loop_method)
        return MyUDPServer(server=udp, loop_method=loop_method)

    def run(self) -> None:
        loop = self.loop
        loop.run_until_complete(self.server)
        loop.run_forever()
