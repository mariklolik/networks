import socket
import struct
from time import sleep


class Sender:
    def __init__(self, multicast_group: str, port: int):
        self.multicast_group = multicast_group
        self.port = port
        # AF_INET - IPv4 protocol, SOCK_DGRAM - datagram UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # ttl to bytes
        ttl = struct.pack('b', 1)
        # set ttl
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    def send_message(self) -> None:
        try:
            while True:
                message = f'appid - {id(self)}'
                self.sock.sendto(message.encode(), (self.multicast_group, self.port))
                print(f'Sent: {message}')
                sleep(2)
        finally:
            self.close()

    def close(self):
        self.sock.close()
