def collect_phone_number():
    phone_number = input("type your number: ").strip()
    while not phone_number.isdigit() or len(phone_number) != 11:
        print("Invalid Phone nmbeer")
        phone_number = input("type your number: ").strip()

    return phone_number


def collect_name():
    name = input("type your name( or q to quit): ").strip().lower()
    while not name.isalpha():
        print("Invalid Name")
        name = input("type your name( or q to quit): ").strip().lower()
        
    return name


def store_contacts():    
    while True:
        name = collect_name
        #store names
        
        if name == 'quit' or name == 'q':
            break
        #collect phone number with function
        phone_number = collect_phone_number()
            
        contacts[name.capitalize()] = phone_number

def retrieve_contacts():
     while True:
        name = input("type your name( or q to quit): ").strip().lower()
        if name == 'quit' or name == 'q':
            break
        
        try:
            print(name, contacts[name.capitalize()])

        except:
            print("The key does not exist")


        
def main():
    #create a contact dictionary
    global contact
    contacts = {}
    
    #collect and store contacts in dictionary
    print("STORAGE MODE")
    
    store_contacts()
    print(f"contact = (contacts)")

    #help get or retrieve contacts from the dictionary
    print('\n RETRIVAL MODE')
    retrieve_contacts()


if __name__ == '__main__':
    main()
