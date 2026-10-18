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
        "\n"
        "╔══════════════════════════════════╗\n"
        "║               CREQ               ║\n"
        "║     Access Card Management       ║\n"
        "╠══════════════════════════════════╣\n"
        "║  1.  📝 Create Request           ║\n"
        "║  2.  🔎 View Request             ║\n"
        "║  3.  ✓  Approve Request          ║\n"
        "║  4.  🎫 Issue Card               ║\n"
        "║  5.  ↩  Return Card              ║\n"
        "║  6.  📋 List Requests            ║\n"
        "║  7.  🚪 Exit                     ║\n"
        "╚══════════════════════════════════╝\n"
        "  Select an option [1-7]: "
    ).strip()

    if choice not in options:
        print(
            "\n  ⚠ Invalid menu selection."
            "\n  Please enter a number between 1 and 7.\n"
        )
        return "main_menu"

    return options[choice]


def generate_id(ids: list[str]) -> str:
    number = 1
    request_id = f"A{number:03d}"

    while request_id in ids:
        number += 1
        request_id = f"A{number:03d}"

    return request_id


def get_card_type() -> str | None:
    options = {
        "1": "visitor",
        "2": "student",
        "3": "staff",
    }

    choice = input(
        "\n"
        "╭──────────────────────────────────╮\n"
        "│            CARD TYPE             │\n"
        "├──────────────────────────────────┤\n"
        "│  1.  👤 Visitor Card             │\n"
        "│  2.  🎓 Student Card             │\n"
        "│  3.  💼 Staff Card               │\n"
        "╰──────────────────────────────────╯\n"
        "  Select card type [1-3]: "
    ).strip()

    if choice not in options:
        print(
            "\n  ⚠ Invalid card type selection."
            "\n  Choose Visitor (1), Student (2), or Staff (3)."
            "\n  Please try again.\n"
        )
        return None

    return options[choice]