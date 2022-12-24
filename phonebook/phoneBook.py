pbList = []
phoneBooks = {}

Current_pb = 0   
choice = 1 
def menu():
   
    print("********************************************************************")
    print("\t\t\tPhoneBook", flush=False)
    print("********************************************************************")
    print("\tyou currently have " + str(len(phoneBooks.keys())) + "\tphonebooks saved")
    if len(phoneBooks)>0 :
        pbList = list(phoneBooks.keys())
        print(pbList)
    print("1. Create phonebook")
    print("2. Select phonebook")
    print("3. Add contact")
    print("4. Modify contact")
    print("5. Display contact")
    print("6. Search for a contact")
    print("7. Delete contact")
    print("8. Delete Phonebook")
    print("9. Exit phonebook")
 
    # Out of the provided 6 choices, user needs to enter any 1 choice among the 6
    # We return the entered choice to the calling function wiz main in our case
    choice = int(input("Please enter your choice: "))
     
    return choice
def create_phonebook():
    #num_pb += 1
    pb_name = str(input("Enter the phonebook name: "))
    phoneBooks[pb_name] = []
    
    return pb_name


def select_phonebook() :
    print("This is a list of the available phonebooks \n")
    print(str(pbList))  
    name = str(input("Please enter the name of the phone book you want to select : "))   
    if name in pbList :
         print("the "+ name + " phonebook is selected")
         return name 
    else :
         print("you entered a wrong name")    
        
def add_contact(current):
    # Adding a contact is the easiest because all you need to do is:
    # append another list of details into the already existing list
    
    new_contact = {}
    
        
    first = (str(input("Enter first name: ")))
    
    surname = (str(input("Enter surname name: ")))
    name = first + ' ' + surname
    new_contact[name] = {}
    number = (input("Enter number: "))
    if len(number) > 10 :
        new_contact[name]['phone_number'] =  number 
        print("number was added to contact " + str(name) + " successfully")
    else :
        print("what you entered is not valid")
    
    
    new_contact[name]['email'] = str(input("Enter e-mail address: "))
    
    new_contact[name]['gender'] = str(input("Enter gender: "))
 
       
    print("the contact is saved")
    print(new_contact)
    phoneBooks[current].append(new_contact)
    # And once you modify the list, you return it to the calling function wiz main, here.
    
def modify_contact(current) :
    printf("please enter the name of the contact you want to modify")
    contact = (str(input("Enter contact name: ")))
    modified_contact= {}
    
    first = (str(input("Enter first name: ")))
    
    surname = (str(input("Enter surname name: ")))
    name = first + ' ' + surname
    modified_contact[name] = {}
    number = (input("Enter number: "))
    if len(number) > 10 :
        modified_contact[name]['phone_number'] =  number 
        print("number was added to contact " + str(name) + " successfully")
    else :
        print("what you entered is not valid")
    
    
    modified_contact[name]['email'] = str(input("Enter e-mail address: "))
    
    modified_contact[name]['gender'] = str(input("Enter gender: "))
 
       
    
    print(modified_contact)
    phoneBooks[current].append(modified_contact)
    print("edit is saved")
    phoneBooks[current].remove(contact)
    #dictionary[new_key] = dictionary.pop(old_key)
    print("the phone book after modification")
    print(phoneBooks[current])
    
    
def display_contact(current):
    
    print("please enter the name of the contact you want to display")
    name = (str(input("Enter contact name: ")))   
    for contact in phoneBooks[current] :
        #print(type(contact))
        #print(contact)
        for contact_name in contact.keys():
            #print(type(contact_name))
            if str(contact_name) == str(name):
   
                print("name " + str(contact_name) + " "+ str(contact[contact_name]))
            else :
                print("you entered a wrong name")
                
                


def search_contact(current):
    
    print("please enter the name of the contact you want to display")
    name = (str(input("Enter contact name: ")))   
    for contact in phoneBooks[current] :
        #print(type(contact))
        #print(contact)
        for contact_name in contact.keys():
            #print(type(contact_name))
            if str(contact_name) == str(name):
   
                print("the name entered was found in phonebook "+ str(current) )
            else:
                print("the name entered was not found")
               
  
def delete_contact(current):
    
    print("please enter the name of the contact you want to delete")
    name = (str(input("Enter contact name: ")))   
    for contact in phoneBooks[current] :
        #print(type(contact))
        #print(contact)
        for contact_name in contact.keys():
            #print(type(contact_name))
            if str(contact_name) == str(name):
                del contact_name
                print("the contact you entered is deleted") 
            else :
                print("you entered a wrong name")

def delete_phonebook():
    print("please enter the name of the phonebook to be deleted")
    name = (str(input("Enter phonebook name: ")))  
    if name in phoneBooks.keys():
        del phoneBooks[name]
        print("the phonebook has been deleted successfully")
    else:
        print("the name you entered was not found in the phonebooks list")







   # main function

while 0 < choice <=  8 :
    choice = menu()
        
    if choice == 1 :
        Current_pb = create_phonebook()
    elif choice == 2 :
        pbList = list(phoneBooks.keys())
        Current_pb = select_phonebook() 
    elif choice == 3 :
        if Current_pb == 0 :
            print("there is no phonebook selected please create one first")
        else : 
            
            print("you are editing "+ str(Current_pb) + " phonebook")
            add_contact(Current_pb)
    elif choice == 4 :
        if Current_pb == 0 :
            print("there is no phonebook selected please create one first")
        else : 
            print("you are editing "+ str(Current_pb) + " phonebook")
            modify_contact(Current_pb)
    elif choice == 5 :
        if Current_pb == 0 :
            print("there is no phonebook selected please create one first")
        else : 
            print( str(Current_pb) + " phonebook is selected")
            display_contact(Current_pb)
    elif choice == 6 :
        if Current_pb == 0 :
            print("there is no phonebook selected please create one first")
        else : 
            print( str(Current_pb) + " phonebook is selected")
            search_contact(Current_pb)
    elif choice == 7 :
        if Current_pb == 0 :
            print("there is no phonebook selected please create one first")
        else : 
            print( str(Current_pb) + " phonebook is selected")
            delete_contact(Current_pb)
    elif choice == 8 :
        delete_phonebook()
    elif choice != 9 : 
        print("you entered a wrong choice")
          
          
    