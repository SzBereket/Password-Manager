# da = {'a' : 'akshat', 'b' : 'bhuvan', 'c': 'chandan'}

# print(da["b"])

from webbrowser import get
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://szb123:szb123@cluster0.ykeob.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]
mycol = mydb["Accounts"]
titlename1 = "Facebook"
for x in mycol.find():
    # print(x)
    a = mycol.find()
    print(a.collection)
    # print("hi")

    # if a.==titlename1:
    #     print(mycol.find) 
# print(type(mycol.find))