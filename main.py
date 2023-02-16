from argparse import ArgumentParser
from receiver import Receiver
from sender import Sender


parser = ArgumentParser(description='Make sure both the devices are connected to the same network (wifi or hotspot) also run "receive" mode first followed by "send"')

parser.add_argument('mode', help='either send or receive')
parser.add_argument('host', help='host IP address')
parser.add_argument('path', help='if mode=send then enter the path where the file is located, else if mode=receive enter the destination path along with the filename including the extension')
parser.add_argument('-p', '--port', type=int, help='optional argument used to change the port')

port = 8010

args = parser.parse_args()

if args.port != None:
    port = args.port

sender = Sender(args.host, port)
receiver = Receiver(args.host, port)

if args.mode == 'receive':
    receiver.listen()
    receiver.download(args.path)

elif args.mode == 'send':
    sender.connect()
    sender.send(args.path)

else:
    print('Invalid input!')