import assistant


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = assistant.parse_input(user_input)
        if command in ["close", "exit", "bye", "q"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(assistant.add_contact(args, contacts))
        elif command == "change":
            print(assistant.change_contact(args, contacts))
        elif command == "phone":
            print(assistant.show_phone(args, contacts))
        elif command == "all":
            print(assistant.show_all(args, contacts))
        else:
            print(f"Invalid command.{command}")


if __name__ == "__main__":
    main()
