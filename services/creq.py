from services.utils import generate_id, get_card_type

from typing import TypedDict
from pathlib import Path
import json

DB_DIR = Path(__file__).resolve().parent.parent / "data"
DB_FILE_PATH = DB_DIR / "requests.json"


class TicketDict(TypedDict):
    id: str
    fellow_id: str
    card_type: str
    status: str
    approved_by: str


class Creq:
    def __init__(self) -> None:
        self.requests: dict[str, TicketDict] = {}

    def create_request(self) -> str | None:
        print(
            "\n╔══════════════════════════════════╗\n"
            "║         📝 CREATE REQUEST        ║\n"
            "╚══════════════════════════════════╝"
        )

        fellow_id = input("  Fellow ID: ").strip()

        if not fellow_id:
            print("\n  ⚠ Fellow ID cannot be empty.\n")
            return

        card_type = get_card_type()

        if not card_type:
            return

        request_id = generate_id(list(self.requests))

        self.requests[request_id] = {
            "id": request_id,
            "fellow_id": fellow_id,
            "card_type": card_type,
            "status": "requested",
            "approved_by": "None"
        }

        print(
            "\n  ✓ REQUEST CREATED SUCCESSFULLY\n"
            "  ──────────────────────────────\n"
            f"  Request ID : {request_id}\n"
            f"  Fellow ID  : {fellow_id}\n"
            f"  Card Type  : {card_type.capitalize()}\n"
            "  Status     : Requested\n"
        )

        return request_id

    def view_request(self):
        if not self.requests:
            print("\n  ℹ No requests found. Create a request first.\n")
            return

        print(
            "\n╔══════════════════════════════════╗\n"
            "║          🔎 VIEW REQUEST         ║\n"
            "╚══════════════════════════════════╝"
        )

        request_id = input("  Request ID: ").strip()

        if not request_id:
            print("\n  ⚠ Request ID cannot be empty.\n")
            return

        if request_id not in self.requests:
            print(f"\n  ✗ No request found with ID '{request_id}'.\n")
            return

        request = self.requests[request_id]

        print(
            "\n╭────────── REQUEST DETAILS ───────╮\n"
            f"  Request ID  : {request['id']}\n"
            f"  Fellow ID   : {request['fellow_id']}\n"
            f"  Card Type   : {request['card_type'].capitalize()}\n"
            f"  Status      : {request['status'].capitalize()}\n"
            f"  Approved By : {request['approved_by']}\n"
            "╰─────────────────────────────────╯\n"
        )

    def approve_request(self):
        if not self.requests:
            print("\n  ℹ No requests available for approval.\n")
            return

        print(
            "\n╔══════════════════════════════════╗\n"
            "║        ✓ APPROVE REQUEST         ║\n"
            "╚══════════════════════════════════╝"
        )

        request_id = input("  Request ID: ").strip()

        if not request_id:
            print("\n  ⚠ Request ID cannot be empty.\n")
            return

        if request_id not in self.requests:
            print(f"\n  ✗ No request found with ID '{request_id}'.\n")
            return

        staff_id = input("  Approving Staff ID: ").strip()

        if not staff_id:
            print("\n  ⚠ Staff ID cannot be empty.\n")
            return

        request = self.requests[request_id]

        if request["status"] != "requested":
            print(
                f"\n  ⚠ Request '{request_id}' cannot be approved.\n"
                f"  Current status: {request['status'].capitalize()}\n"
                f"  Approved by: {request['approved_by']}\n"
            )
            return

        request["status"] = "approved"
        request["approved_by"] = staff_id

        print(
            "\n  ✓ REQUEST APPROVED\n"
            "  ──────────────────────────────\n"
            f"  Request ID : {request_id}\n"
            f"  Approved By: {staff_id}\n"
            "  Status     : Approved\n"
        )

    def issue_card(self):
        if not self.requests:
            print("\n  ℹ No requests available for card issuance.\n")
            return

        print(
            "\n╔══════════════════════════════════╗\n"
            "║          🎫 ISSUE CARD           ║\n"
            "╚══════════════════════════════════╝"
        )

        request_id = input("  Request ID: ").strip()

        if not request_id:
            print("\n  ⚠ Request ID cannot be empty.\n")
            return

        if request_id not in self.requests:
            print(f"\n  ✗ No request found with ID '{request_id}'.\n")
            return

        request = self.requests[request_id]

        if request["status"] != "approved":
            print(
                "\n  ⚠ Card issuance denied.\n"
                f"  Current status: {request['status'].capitalize()}\n"
                "  The request must be approved before a card can be issued.\n"
            )
            return

        request["status"] = "issued"

        print(
            "\n  ✓ CARD ISSUED SUCCESSFULLY\n"
            "  ──────────────────────────────\n"
            f"  Request ID : {request_id}\n"
            f"  Issued To  : {request['fellow_id']}\n"
            f"  Card Type  : {request['card_type'].capitalize()}\n"
            "  Status     : Issued\n"
        )

    def return_card(self):
        if not self.requests:
            print("\n  ℹ No requests available for card return.\n")
            return

        print(
            "\n╔══════════════════════════════════╗\n"
            "║          ↩ RETURN CARD           ║\n"
            "╚══════════════════════════════════╝"
        )

        request_id = input("  Request ID: ").strip()

        if not request_id:
            print("\n  ⚠ Request ID cannot be empty.\n")
            return

        if request_id not in self.requests:
            print(f"\n  ✗ No request found with ID '{request_id}'.\n")
            return

        request = self.requests[request_id]

        if request["status"] != "issued":
            print(
                "\n  ⚠ Card cannot be returned.\n"
                f"  Current status: {request['status'].capitalize()}\n"
                "  Only issued cards can be returned.\n"
            )
            return

        request["status"] = "returned"

        print(
            "\n  ✓ CARD RETURNED SUCCESSFULLY\n"
            "  ──────────────────────────────\n"
            f"  Request ID : {request_id}\n"
            f"  Returned By: {request['fellow_id']}\n"
            "  Status     : Returned\n"
        )

    def list_requests(self):
        if not self.requests:
            print("\n  ℹ No requests found. Nothing to display.\n")
            return

        print(
            "\n╔══════════════════════════════════════════════════════════════╗\n"
            "║                       📋 ALL REQUESTS                       ║\n"
            "╚══════════════════════════════════════════════════════════════╝"
        )

        headers = (
            f"{'ID':<8}"
            f"{'Fellow ID':<16}"
            f"{'Card Type':<12}"
            f"{'Status':<14}"
            f"{'Approved By':<14}"
        )

        print(f"\n  {headers}")
        print("  " + "─" * len(headers))

        for request in self.requests.values():
            print(
                f"  {request['id']:<8}"
                f"{request['fellow_id']:<16}"
                f"{request['card_type'].capitalize():<12}"
                f"{request['status'].capitalize():<14}"
                f"{request['approved_by']:<14}"
            )

        print(f"\n  Total requests: {len(self.requests)}\n")

    def load(self):
        DB_DIR.mkdir(parents=True, exist_ok=True)

        try:
            with open(DB_FILE_PATH, "r", encoding="utf-8") as file:
                self.requests = json.load(file)

        except FileNotFoundError:
            print(
                "\n  ℹ No existing requests database found.\n"
                "  A new database will be created when saved.\n"
            )

        except json.JSONDecodeError:
            print(
                "\n  ✗ The requests database contains invalid JSON.\n"
                "  Existing data could not be loaded.\n"
            )

        except OSError as error:
            print(f"\n  ✗ Could not read the requests database: {error}\n")

        else:
            print(f"\n  ✓ Loaded {len(self.requests)} request(s).\n")

    def save(self):
        DB_DIR.mkdir(parents=True, exist_ok=True)

        try:
            with open(DB_FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(self.requests, file, indent=4)

        except (OSError, TypeError) as error:
            print(f"\n  ✗ Could not save requests: {error}\n")

        else:
            print(f"\n  ✓ Saved {len(self.requests)} request(s).\n")