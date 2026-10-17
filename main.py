from services.utils import get_main_menu_opt

def creq_runner():
    state = "main_menu"

    print("\nLoading data...\n")

    while state != "exit":
        if state == "main_menu":
            state = get_main_menu_opt()

        elif state == "create_request":
            print("Creating request")
            state = "main_menu"

        elif state == "view_request":
            print("Viewing request")
            state = "main_menu"

        elif state == "approve_request":
            print("Approving request")
            state = "main_menu"

        elif state == "issue_card":
            print("Issuing card")
            state = "main_menu"

        elif state == "return_card":
            print("Returning card")
            state = "main_menu"

        elif state == "list_request":
            print("Listing requests")
            state = "main_menu"

        else:
            print("\nInvalid selection.Try again...\n")

    print("\nSaving session\n")

    print("\nExiting...\n")

creq_runner()