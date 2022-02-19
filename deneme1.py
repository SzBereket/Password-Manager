# da = {'a' : 'akshat', 'b' : 'bhuvan', 'c': 'chandan'}

# print(da["b"])

# from webbrowser import get
# import pymongo
import random
from xml.dom.pulldom import CHARACTERS
# myclient = pymongo.MongoClient("mongodb+srv://szb123:szb123@cluster0.ykeob.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# mydb = myclient["mydatabase"]
# mycol = mydb["Accounts"]
# print("Write Title Name: ")
# titlename1 = input()
# for x in mycol.find():
#     # print(x['Title']) 
#     if x['Title'] == titlename1:
#         print(x['Title']+"  "+x['Password'])



    # print(x)
    # a = mycol.find()
    # print(a.collection)
    # print("hi")

    # if a.==titlename1:
    #     print(mycol.find) 
# print(type(mycol.find))
import string
import random


## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
	## length of password from the user


	## shuffling the characters
random.shuffle(characters)
	
	## picking random characters from the list
password = []
for i in range(10):
	password.append(random.choice(characters))

	## shuffling the resultant password
random.shuffle(password)

	## converting the list to string
	## printing the list
print("".join(password))
