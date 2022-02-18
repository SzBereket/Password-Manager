import pymongo

myclient = pymongo.MongoClient("mongodb+srv://szb123:szb123@cluster0.ykeob.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]
mycol = mydb["Accounts"]

# mydict = { "ID": "1","Title": "Twitter", "Nickname": "sabrideneme123", "Password": "sifrem" }

# mycol.insert_one(mydict)
print("          Welcome        ")
print("***************************")
print("What You Wanna Do?\n***************************\n1.See Your Accounts Informations\n2.Create New Account\n3.Add New Accounts\n4.Change Your Accounts Information\n5.Remove Your Accounts\n9.Leave The Program\n***************************")

while True:
    print("Select the transaction: ")
    selection1 = input()
    if selection1 == 9:
        print("Have Good Day")
        break    
    elif int(selection1) ==1:
        print("1. All Accounts\n2. Select Account")
        see1 = input()
        if int(see1) == 1 : 
            for x in mycol.find():
                print(x)
        elif int(see1) ==2: 
            print("Write title name:")
            titlename1 = input()
            for i in mycol.find:
             print("hi")
             if mycol.find["Title"]==titlename1:
              print(mycol.find) 
    elif int(selection1) ==2:
        print("are u sureeee ")
    
    elif int(selection1) ==3:
        print("are u sureeee ")
    
    elif int(selection1) ==4:
        print("are u sureeee ")
    
    elif int(selection1) ==5:
        print("are u sureeee ")
    
    else:
        print("Wrong Choice")
