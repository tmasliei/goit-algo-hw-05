def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such name exists"
        except IndexError:
            return "The index in the sequence is out of range"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args,contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact upded."

@input_error
def show_phone(contacts):
    pass

@input_error
def show_all(args,contacts):
    pass

def main():
    contacts = {}
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
        elif command =="change":
            print(change_contact(args,contacts))
        elif command == "phone":
            print(show_phone(contacts))
        elif command == "all": 
            print(show_all(args,contacts))   
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()