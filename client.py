import zmq, ipaddress as ip
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.1.81:50001")

for i in range(100):
    msg = "msg %s" % i
    socket.send_string(msg)
    print("Sending", msg)
    msg_in = socket.recv()
