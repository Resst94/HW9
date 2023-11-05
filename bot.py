# Dictionary to store contacts (username: phone number)
contacts = {}

# Decorator for handling input errors
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"
    return wrapper

# Function to greet the user
def hello():
    return "How can I help you?"

# Function to add a new contact
@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}"

# Function to change the phone number of an existing contact
@input_error
def change_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} changed to {phone}"
    else:
        return f"Contact with name {name} not found"

# Function for outputting the phone number of a contact
@input_error
def phone_contact(name):
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"Contact with name {name} not found"

# Function to display all contacts
def show_all_contacts():
    if contacts:
        result = "All contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result
    else:
        return "Contact list is empty"

# Function to terminate the bot
def exit_bot():
    return "Good bye!"

# The main function of the bot
def main():
    while True:
        command = input("Enter a command: ").lower()

        if command == "hello":
            print(hello())
        elif command.startswith("add "):
            _, rest_of_command = command.split(" ", 1)
            try:
                name, phone = rest_of_command.split(" ")
                print(add_contact(name, phone))
            except ValueError:
                print("Invalid command format. Please use 'add [name] [phone]' format.")
        elif command.startswith("change "):
            _, rest_of_command = command.split(" ", 1)
            try:
                name, phone = rest_of_command.split(" ")
                print(change_contact(name, phone))
            except ValueError:
                print("Invalid command format. Please use 'change [name] [phone]' format.")
        elif command.startswith("phone "):
            _, name = command.split(" ", 1)
            print(phone_contact(name))
        elif command == "show all":
            print(show_all_contacts())
        elif command in ["good bye", "close", "exit"]:
            print(exit_bot())
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
