def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            return "Give me name and phone please"
        except KeyError:
            return "User not found"
        except IndexError:
            return "Enter user name"
        except Exception:
            return "Please enter right command"

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def validate_args(args):
    if len(args) != 2 or not args[1].isdigit():
        return False
    return True


@input_error
def add_contact(args, contacts):
    if not validate_args(args):
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return f"Contact: {name} was added."


@input_error
def change_contact(args, contacts):
    if not validate_args(args):
        raise ValueError
    name, phone = args
    if not name in contacts.keys():
        return f"Name: {name} not found!"
    contacts[name] = phone
    return f"Contact: {name} was updated."


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if not name in contacts:
        return f"Name: {name} not found!"
    return contacts[name]


@input_error
def show_all(args, contacts):
    formatted_list = []
    if len(args) != 0:
        raise Exception
    for name, phone in contacts.items():
        formatted_list.append(f"{name}: {phone}\n")

    return "".join(formatted_list)


if __name__ == "__main__":
    print("Welcome to the assistant function!")
