import pymongo
import random
import string
from faker import Faker
import time
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
                print(x['Title']+" "+x['Password'])
        elif int(see1) ==2: 
            print("Write title name:")
            titlename1=input()
            for x in mycol.find():
                # print(x['Title']) 
                if x['Title'] == titlename1:
                    print(x['Title']+"  "+x['Password'])
    elif int(selection1) ==2:
        print("Write the new account Title:")
        newtitle = input()
        print("Write the new account Nickname:")
        newnickname:input()
        print("1.Automatically generate password.\n2.Write manual password")
        passchoice=input()
        if int(passchoice) == 1:
            fake = Faker()
            print(fake.password())
            time.sleep(5)
            savechoice1 = input("Do you want me to save this data?\n 1.Yes \n 2.No")
            if int(savechoice1)== 1:
                x= mycol.find.last #SON ID'yi bulup onu id kısmına yazdıracaksın unutma
                mydict = { "ID": "1","Title": newtitle, "Nickname": newnickname, "Password": fake.password() }
                mycol.insert_one(mydict)
    
    elif int(selection1) ==3:
        print("are u sureeee ")
    
    elif int(selection1) ==4:
        print("are u sureeee ")
    
    elif int(selection1) ==5:
        print("are u sureeee ")
    
    else:
        print("Wrong Choice")
