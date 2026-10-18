def get_main_menu_opt():
    options = {
        "1": "create_request",
        "2": "view_request",
        "3": "approve_request",
        "4": "issue_card",
        "5": "return_card",
        "6": "list_request",
        "7": "exit",
    }

    choice = input(
        "\n======== CREQ ========\n"
        "1. Create request\n"
        "2. View request\n"
        "3. Approve request\n"
        "4. Issue card\n"
        "5. Return card\n"
        "6. List requests\n"
        "7. Exit\n"
        "____________________________\n"
        "Select an option(1-7): "
    )

    if choice not in options:
        print("\nInvalid selection. Try again\n")
        return "main_menu"
    
    return options[choice]

def generate_id(ids: list[str]):
    number = 1

    id = f"A{number:03d}"

    while id in ids:
        number += 1
        id = f"A{number:03d}"

    return id

def get_card_type() -> str | None:
    options = {
        "1": "visitor",
        "2": "student",
        "3": "staff"
    }

    choice = input(
        "\n----- Select card type -----\n"
        "1. Vistor\n"
        "2. Student\n"
        "3. Staff\n"
        "______________________________\n"
        "Select an option(1-3): "
    )

    if choice not in options:
        print("\nInvalid card type selection\n")
        return
    
    return options[choice]