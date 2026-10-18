from services.utils import get_main_menu_opt

from services.creq import Creq

creq = Creq()

def creq_runner():
    state = "main_menu"

    creq.load()

    while state != "exit":
        if state == "main_menu":
            state = get_main_menu_opt()

        elif state == "create_request":
            creq.create_request()
            state = "main_menu"

        elif state == "view_request":
            creq.view_request()
            state = "main_menu"

        elif state == "approve_request":
            creq.approve_request()
            state = "main_menu"

        elif state == "issue_card":
            creq.issue_card()
            state = "main_menu"

        elif state == "return_card":
            creq.return_card()
            state = "main_menu"

        elif state == "list_request":
            creq.list_requests()
            state = "main_menu"

        else:
            print(
                "\n  ⚠ Invalid menu selection."
                "\n  Please choose a valid option from the menu.\n"
            )

    creq.save()

    print(
        "╔══════════════════════════════════╗\n"
        "║          CREQ                    ║\n"
        "║   👋 Exiting application...      ║\n"
        "╚══════════════════════════════════╝\n"
    )

creq_runner()