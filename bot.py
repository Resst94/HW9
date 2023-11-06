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
        except Exception as e:
            return f"Error: {str(e)}"
    return wrapper

# Function to greet the user
def hello():
    return "How can I help you?"

# Function to add a new contact
@input_error
def add_contact(command):
    parts = command.split(" ")
    if len(parts) == 3:
        name, phone = parts[1], parts[2]
        if name not in contacts:
            contacts[name] = phone
            return f"Contact {name} with number {phone} saved."
        else:
            return "Contact with the same name already exists"
    else:
        raise ValueError

# Function to change the phone number of an existing contact
@input_error
def change_contact(command):
    parts = command.split(" ")
    if len(parts) == 3:
        name, phone = parts[1], parts[2]
        if name in contacts:
            contacts[name] = phone
            return f"Phone number for {name} changed to {phone}."
        else:
            raise KeyError
    else:
        raise ValueError

# Function to output the phone number of a contact
@input_error
def get_phone(command):
    parts = command.split(" ")
    if len(parts) == 2:
        name = parts[1]
        if name in contacts:
            return f"Phone number for {name}: {contacts[name]}"
        else:
            raise KeyError
    else:
        raise ValueError

# Function to display all contacts
@input_error
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
    
# Function to handle unknown commands
@input_error
def unknown_command(command):
    return f"Unknown command: {command}. Please try again."

# Parse and execute the user command
def main():
    while True:
        command = input("Enter command: ").lower().strip()

        if command.lower() == "hello":
            print("How can I help you?")
        elif command.startswith("add "):
            print(add_contact(command))
        elif command.startswith("change "):
            print(change_contact(command))
        elif command.startswith("phone "):
            print(get_phone(command))
        elif command == "show all":
            print(show_all_contacts())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print(unknown_command(command))

if __name__ == "__main__":
    main()
