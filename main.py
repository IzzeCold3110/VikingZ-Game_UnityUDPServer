import time

from Thread import UDPServerThread
from argparse import ArgumentParser

#
# run with: main.py 44545 127.0.0.1
#

_default_address = "0.0.0.0"
_default_port = 44584

parser = ArgumentParser()
parser.add_argument('port', metavar='Port', type=int, nargs='?', help='Port', const=_default_port)
parser.add_argument('address', metavar='Address', type=str, nargs='?', help='Address', const=_default_address)
args = parser.parse_args()


def main():
    server_port = args.port if args.port is not None else _default_port
    server_address = args.address if args.address is not None else _default_address

    try:
        udp_server_thread = UDPServerThread(server_address, server_port, args)
        udp_server_thread.daemon = True
        udp_server_thread.start()
        print("UDP Server at port " + server_address + ":" + str(server_port))
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        print(" - Stopped by User")


if __name__ == '__main__':
    main()
