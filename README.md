# HW9

This is a console bot assistant that will recognize commands entered from the keyboard and respond according to the command entered.

The bot assistant is a prototype of an assistant application. The simplest and most convenient interface at the initial stage of development is the CLI (Command Line Interface) console application.

How it works:

The bot is in an endless loop, waiting for a user command.
The bot ends its work if it encounters the words: "good bye", "close", "exit".
The bot is not sensitive to the case of the entered commands.
The bot accepts commands:
- "hello", Greetings.
- "add ...". This command saves a new contact in the bot's memory. 
- "change ..." This command saves the new phone number of an existing contact to the bot's memory.
- "phone ...." This command displays the phone number for the specified contact in the console. 
- "show all". This command displays all saved contacts with phone numbers in the console.
- "good bye", "close", "exit": with any of these commands, the bot terminates its work.

All user input errors are handled by the input_error decorator. This decorator is responsible for returning messages such as "Enter user name", "Give me name and phone please", etc. The input_error decorator handles exceptions that occur in the handler functions (KeyError, ValueError, IndexError) and returns the appropriate response to the user.

