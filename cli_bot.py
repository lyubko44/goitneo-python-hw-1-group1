def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone for contact {name} has been changed."
    else:
        return f"Contact for {name} does not exist."        

def display_all(contacts):
    if len(contacts) == 0:
        return("There is no saved contacts. Please add them ...")
    else:    
        contacts_list = []
        for name, phone in contacts.items():
            contacts_list.append(f"{name} - {phone}")
        return "\n".join(contacts_list)

def display_phone(args, contacts):
    name = ''.join(args) #I would add here validation if there is one argument, but it's not required
    if name in contacts:
        number = contacts[name]
        return f"Phone for contact {name} is {number}"
    else:
        return f"Contact for {name} does not exist."

def main():
    contacts = {'Lucas': 91679333}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(display_all(contacts))
        elif command == "phone":
            print(display_phone(args, contacts))          
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()