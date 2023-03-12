# MrShare
## To download run "git clone https://github.com/dheerajroy/MrShare.git"
## Description
A minimalistic software used to transfer files between systems connected to the same network
## How to use
### usage:
main.py [-h] [-port PORT] mode host path

Make sure both the devices are connected to the same network (wifi or hotspot) also run "receive" mode first followed
by "send"

### positional arguments:
  mode                  either send or receive\
  host                  host (receiver) IP address\
  path                  if mode=send then enter the path where the file is located, else if mode=receive enter the destination path along with file name and extension
### optional arguments:
  -h, --help            show this help message and exit\
  -p PORT, --port PORT
                        optional argument used to change the port
