contact=[]
import os
print (contact)
while True:
    #add contact
    menu= input ("1, Add Contact \n 2, View Contact \n 3, Delete Contact \n 4, Save Contact \n 5, Exit\n")
    if menu ==("1"):
        for i in range (1):
          name= input ("contact name\n")
          phone= input ("phone number\n")
          email= input (" email address\n")
          print("CONTACT SAVED!")
          contact.append({"name": name, "phone": phone, "email": email,})
          print (contact)
          # view and search for contact
    elif menu==("2"):
       print (contact)   
       search_contact= input (" Do You Want To Search For A Contact")
       if search_contact== "yes" :
          name_search= input ("enter name to search")
          found =False
          for contacts in contact:
             if contacts ["name"]== name_search:
                print (contacts)
                found= True 
       elif  search_contact=="no":
           exit()      
       else:
                found=False
                print("Contact not found ")
    elif menu == ("3"):
       # delete contact
       delete_contact=input ("enter contact name to delete\n")
       didfound= False
       for c in contact:
           if c ["name"] ==delete_contact:
               contact.remove(c)
               print("contact removed ")
               didfound= True
       if didfound== False:
             print ("contact not found")
         # save contact  
    elif menu== ("4"):
        print("File location:", os.getcwd())
        with open("C:/Users/HomePC/Desktop/contact.txt","a") as file:
            for c in contact:
                file.write (c["name"]+"-"+c["phone"]+"-"+c["email"]+"\n")
                print("contact saved")
    elif menu == ("5"):
        exit()            

       


                 
        
