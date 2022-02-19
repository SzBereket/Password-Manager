import pymongo
import random
import string
from faker import Faker
import time
myclient = pymongo.MongoClient("MONGODB CONNECTION NEED IN HERE")
mydb = myclient["mydatabase"]
mycol = mydb["Accounts"]

print("          Welcome        ")
print("****************************")

while True:
    time.sleep(3)
    print("\n\nWhat You Wanna Do?\n***************************\n1.See Your Accounts Informations\n2.Create New Account\n3.Add New Accounts\n4.Change Your Accounts Information\n5.Remove Your Accounts\n9.Leave The Program\n***************************")
    print("Select the transaction: ")
    selection1 = input()
    if int(selection1) == 9:
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
                
                if x['Title'] == titlename1:
                    print(x['Title']+"  "+x['Password'])
    elif int(selection1) ==2:
        list1 =[]
        for x in mycol.find():
            list1.append(x['ID'])
        newid = int(max(list1))+1
        print("Write the new account Title:")
        newtitle = input()
        print("Write the new account Nickname:")
        newnickname1 = input()
        print("1.Automatically generate password.\n2.Write manual password")
        passchoice=input()
        if int(passchoice) == 1:
            fake = Faker()
            print(fake.password())
            time.sleep(5)
            savechoice1 = input("Do you want me to save this data?\n 1.Yes \n 2.No\n")
            if int(savechoice1)== 1:
                
                mydict = { "ID": newid ,"Title": newtitle , "Nickname": newnickname1 , "Password": fake.password() }
                mycol.insert_one(mydict)
                print("Successful")
        elif int(passchoice)==2:
            newpassword = input("Write the your password: ")
            savechoice1 = input("Do you want me to save this data?\n 1.Yes \n 2.No\n")
            if int(savechoice1)== 1:
                mydict = { "ID": newid ,"Title": newtitle , "Nickname": newnickname1 , "Password": newpassword }
                mycol.insert_one(mydict)
                print("Successful")
            
    
    elif int(selection1) ==3:
        list1 =[]
        for x in mycol.find():
            list1.append(x['ID'])
        newid = int(max(list1))+1
        print("Write the new account Title:")
        newtitle = input()
        print("Write the new account Nickname:")
        newnickname1 = input()
        newpassword = input("Write the your password:\n ")
        mydict = { "ID": newid ,"Title": newtitle , "Nickname": newnickname1 , "Password": newpassword }
        mycol.insert_one(mydict)
        print("Successful")

    elif int(selection1) ==4:
        for x in mycol.find():
                print(str(x['ID'])+" "+x['Title']+" "+x['Password'])
        changedata = input("Select Number:\n ")
        for a in mycol.find():
            if a['ID'] == int(changedata):
                c = input("What do you want to update\n1.Title\n2.Nickname\n3.Password\n:")
                if int(c)==1:
                    newtitle2=input("Write New Title:\n")
                    myquery = {"ID" : int(changedata)}    
                    newvalues = { "$set": { "Title": newtitle2 } }
                    mycol.update_one(myquery, newvalues)
                    print("Successful")
                elif int(c)==2: 
                    newnickname2 = input("Write New Nickname")
                    myquery = {"ID" : int(changedata)}    
                    newvalues = { "$set": { "Nickname": newnickname2 } }
                    mycol.update_one(myquery, newvalues)
                    print("Successful")
                elif int(c) ==3:
                    newpswrdchoice=input("1.Automatically generate password.\n2.Write manual password:\n")
                    if int(newpswrdchoice)==1:
                        fake = Faker()
                        print(fake.password())
                        time.sleep(5)
                        savechoice2 = input("Do you want me to save this data?\n 1.Yes \n 2.No:\n")
                        if int(savechoice2) == 1:
                            print("hello world")
                            myquery = {"ID" : int(changedata)}    
                            newvalues = { "$set": { "Password": fake.password() } }
                            mycol.update_one(myquery, newvalues)
                            print("Successful")
                    elif int(newpswrdchoice)==2:
                        newpswrd2=input("Write your New Password: \n")
                        myquery = {"ID" : int(changedata)}    
                        newvalues = { "$set": { "Password": newpswrd2 } }
                        mycol.update_one(myquery, newvalues)
                        print("Successful")

                else:
                    print("Wrong Number")
    
    elif int(selection1) ==5:
        for x in mycol.find():
                print(str(x['ID'])+" "+x['Title']+" "+x['Password'])
        changedata = input("Select Number:\n ")
        for a in mycol.find():
            if a['ID'] == int(changedata):
                z = input("Are you sure you want to delete this Account?\n1.Yes\n2.No: \n")
                if int(z)==1:
                    myquery = {"ID" : int(changedata)}
                    mycol.delete_one(myquery)
                    print("Successful")
                
    else:
        print("Wrong Choice")
