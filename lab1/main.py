import threading
from Sender import Sender
from Receiver import Receiver

if __name__ == "__main__":
    # IPv4 address range (224.0.0.0 through 230.255.255.255) reserved for multicast traffic
    MCAST_GRP = '224.0.0.1'
    MCAST_PORT = 5000

    sender = Sender(MCAST_GRP, MCAST_PORT)
    receiver = None
    t2 = None
    try:
        receiver = Receiver(MCAST_GRP, MCAST_PORT)
    except OSError as e:
        print(f'Another reciever already working on {MCAST_GRP}:{MCAST_PORT}')

    t1 = threading.Thread(target=sender.send_message)
    if receiver:
        t2 = threading.Thread(target=receiver.receive_messages)
    t1.start()
    if t2:
        t2.start()
    t1.join()
    if t2:
        t2.join()
