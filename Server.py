from datetime import datetime


class MyUDPServer:
    def __init__(self, server, loop_method):
        self.server = server
        self.loop = loop_method
        self.server.subscribe(self.on_datagram_received)
        # asyncio.ensure_future(self.do_send(), loop=self.loop)

    @staticmethod
    async def on_datagram_received(data, addr):
        print(datetime.now(), addr, data)

    # async def do_send(self):
    #    while True:
    #        payload = b'd1:ad2:id20:k\xe7\x90\xcd\x0c_R\xfe\x82\xeb\xa8 ' \
    #                  b'x\x14\xb4-\x8e0\xe5\x086:target20:\x11\x8e\xcc,' \
    #                  b'\x89\xa4\x99\xf98E\x98\x7f!\xa7w\rz\x1b\x14de1:q9:find_node1:t2:#K1:y1:qe '
    #
    #        await asyncio.sleep(0.001)
    #        self.server.send(payload, ("router.bittorrent.com", 6881))
