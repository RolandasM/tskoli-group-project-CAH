import json
import urllib.request as u
import socket


jsonurl = "http://tsuts.tskoli.is/2t/2202903449/CAH_JSON/CAH_BASESET.json"
#try:
response = u.urlopen(jsonurl).read()
#except Exception as e:
    #print(type(e))
    #print(e)

joutput = json.loads(response.decode('utf-8'))


print(joutput)



#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#try:
    #mysock.connect(('http://tsuts.tskoli.is', 80))
#except Exception as e:
    #print(type(e))
    #print(e)

#try:
    #mysock.send('GET http://tsuts.tskoli.is/2t/2202903449/CAH_JSON/CAH_BASESET.json')
#except Exception as e:
    #print(type(e))
    #print(e)


#while True:
        #data = mysock.recv(512)
        #if (len(data) < 1 ):
            #break
        #print(data)

#mysock.close()


sampleDatabase = '''

'''