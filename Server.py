#
#   Weather update server
#   Binds PUB socket to tcp://*:5556
#   Publishes random weather updates
#

import zmq
from random import randrange

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
    zipcode = randrange(1, 100000)
    temperature = randrange(-80, 135)
    relhumidity = randrange(10, 60)

    socket.send_string("%i %i %i" % (zipcode, temperature, relhumidity))

"""


import zmq, ipaddress as ip
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://85.220.3.232:50001")

while True:
    msg = socket.recv()
    print("Got", msg)
    socket.send(msg)

"""
