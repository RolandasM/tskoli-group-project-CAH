import MySQLdb as p


"""
def onlyNum(arr, pos):
    if str.isdigit(arr[pos]):
        pos += 1
    else:
        del(arr[pos])
    if len(arr) > pos:
        onlyNum(arr,pos)
"""

c = p.connect(host='tsuts.tskoli.is',user='2202903449', passwd='mypassword', db='2202903449_cah')
cur = c.cursor()
#Are weconnected?
clientFound = False
#clientconnected counter
checkclient = 0
#CHECK IF SPOTS ARE AVAIABLE
while(clientFound != True):

    #cur.execute("USE 2202903449_cah")
    #cur.execute("SHOW TABLES")
    id = 1
    clientcounter = int(1)

    WHATUSERISTHIS = 0
    WHATACTIVEISTHIS = 2
    while(clientcounter < 5 and clientFound != True):

        cur.execute("select id from clientsconnected")

        userID = cur.fetchall()
        uid = userID[WHATUSERISTHIS]
        cuID = int(uid[0])

        print(type(userID))
        print(userID)
        print("^userid")

        #There once was a dream called rome
        #onlyNum(userID,0)



        print(userID)
        cur.execute("select active from clientsconnected")
        active = str(cur.fetchall())
        print(active)
        aa = active[WHATACTIVEISTHIS]# +6
        print(aa)
        print(type(cuID))
        print(cuID)
        print(type(clientcounter))
        print(clientcounter)



        if(cuID == clientcounter and aa == '0' ):

            print("user is not active")
            print(type(id))
            print(cuID)
            print(type(cuID))
            #cur.execute('insert into white_cards (text, card_set_id) values (%s, %s)', (text, card_set_id))
            #c.commit()
            printid = str(id)
            printclientcounter = str(clientcounter)
            print("THIS IS ID: " + printid)
            print("THIS IS CLIENTCOUNTER: " + printclientcounter)
            ACTIVATECLIENT = 1
            print(ACTIVATECLIENT)
            print(type(ACTIVATECLIENT))
            print("ACT ^")
            print(id)
            print(type(id))
            print("ID ^")
            cur.execute('update clientsconnected set active = %s where id = %s',(ACTIVATECLIENT,id))
            #cur.execute('update clientsconnected set active = 1 where id = 1')
            c.commit()
            #cursor.execute ("UPDATE tblTableName SET Year=%s, Month=%s, Day=%s, Hour=%s, Minute=%s WHERE Server='%s' " % (Year, Month, Day, Hour, Minute, ServerID))
            c.commit()
            print("Activating client 1")

            whatuser = str(checkclient +1)
            print("User " + whatuser + " has been activated")

            cur.execute("select active from clientsconnected")
            active = str(cur.fetchall())
            clientFound = True

        else:
            WHATACTIVEISTHIS = WHATACTIVEISTHIS + 6
            id = id + 1
            clientcounter = clientcounter +1
            WHATUSERISTHIS = WHATUSERISTHIS + 1
            whatuser = str(checkclient +1)
            print("User " + whatuser + " has already been activated")
            nextuser = str(checkclient + 2)
            print("trying user:  " + nextuser)

            checkclient = checkclient +1
            #clientFound = True



result = str(active[2])
print("1 = active; 0 = inactive. And it is : " + result)