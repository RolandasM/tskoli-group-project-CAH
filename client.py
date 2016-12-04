import random, json as j, urllib.request as u, pprint, pymysql as p
#
#
#
#
#######
c = p.connect(host='tsuts.tskoli.is', port=3306, user='2202903449', passwd='mypassword', db='2202903449_cah')
cur = c.cursor()

#Are weconnected?
clientFound = False
#clientconnected counter
checkclient = 0
#CHECK IF SPOTS ARE AVAIABLE
while(clientFound != True):

    #cur.execute("USE 2202903449_cah")
    #cur.execute("SHOW TABLES")

    cur.execute("select id from clientsconnected")

    userID = str(cur.fetchall())
    #print(userID)
    #print(userID[2])

    cur.execute("select active from clientsconnected")

    active = str(cur.fetchall())

    if(userID[2] == '1' and active[2] == '0' ):
        print("user is not active")

        activate = 1
        id = (checkclient + 1)
        print(type(id))
        print(type(activate))
        #cur.execute('insert into white_cards (text, card_set_id) values (%s, %s)', (text, card_set_id))
        #c.commit()
        cur.execute('update clientsconnected set active = 1 where id = 1')
        c.commit()
        print("Activating client 1")

        whatuser = str(checkclient +1)
        print("User " + whatuser + " has been activated")

        cur.execute("select active from clientsconnected")
        active = str(cur.fetchall())
        clientFound = True

    else:
        whatuser = str(checkclient +1)
        print("User " + whatuser + " has already been activated")
        nextuser = str(checkclient + 2)
        print("trying user:  " + nextuser)

        checkclient = checkclient +1
        clientFound = True


result = str(active[2])
print("1 = active; 0 = inactive. And it is : " + result)

    #with open('http://tsuts.tskoli.is/2t/2202903449/CAH_JSON/userOne.json', 'w') as f:
        #j.dump(data,f,ensure_ascii=False)

urlCAHdb = "http://tsuts.tskoli.is/2t/2202903449/CAH_JSON/anotherCAHjsonDB.json"

reponseCAH = u.urlopen(urlCAHdb).read()

dataCAH = j.loads(reponseCAH.decode('utf-8'))



## trying pretty print ##

pp = pprint.PrettyPrinter(indent=4, depth=6)



"""
import zmq, ipaddress as ip
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.1.81:50001")

for i in range(100):
    msg = "msg %s" % i
    socket.send_string(msg)
    print("Sending", msg)
    msg_in = socket.recv()
"""
