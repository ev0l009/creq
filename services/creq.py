from services.utils import generate_id, get_card_type

from typing import TypedDict

from pathlib import Path
import json

DB_DIR = Path(__file__).resolve().parent.parent/"data"
DB_FILE_PATH = DB_DIR/"requests.json"

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
            "\n----- Create Request -----\n"
        )
        fellow_id = input("Fellow ID: ")

        if not fellow_id.strip():
            print("\nFellow ID cannot be empty\n")
            return
        
        card_type = get_card_type()

        if not card_type:
            return
        
        ids: list[str] = [id for id in self.requests]
        id = generate_id(ids)

        self.requests[id] = {
            "id": id,
            "fellow_id": fellow_id,
            "card_type": card_type,
            "status": "requested",
            "approved_by": "None"
        }

        print(
            "\nRequest created successfully.\n"
            f"Request ID: {id}\n"
        )

    def view_request(self):
        if not self.requests:
            print("\nThere are no requests yet.\n")
            return
        
        print(
            "\n----- View Request -----\n"
        )
        
        request_id = input("Request ID: ")

        if not request_id.strip():
            print("\nRequest ID cannot be empty.\n")
            return

        if request_id not in self.requests:
            print("\nInvalid request ID.\n")
            return
        
        request = self.requests[request_id]

        print(
            f"\nRequest Details\n"
            "----------------------\n"
            f"Request ID: {request['id']}\n"
            f"Fellow ID: {request['fellow_id']}\n"
            f"Card Type: {request['card_type'].capitalize()}\n"
            f"Status: {request['status'].capitalize()}\n"
            f"Approved by: {request['approved_by']}"
        )

    def approve_request(self):
        if not self.requests:
            print("\nThere are no requests yet.\n")
            return

        print(
            "\n----- Approve Request -----\n"
        )

        request_id = input("\nRequest ID: ")

        if not request_id.strip():
            print("\nRequest ID cannot be empty.\n")
            return

        if request_id not in self.requests:
            print("\nInvalid request ID.\n")
            return
        
        staff_id = input("\nStaff ID: ")

        if not staff_id.strip():
            print("\nRequest ID cannot be empty.\n")
            return
        
        request = self.requests[request_id]

        if request["status"] != "requested":
            print(f"\nRequest {request_id} has already been approved by {request['approved_by']}.\n")
            return
        
        request["status"] = "approved"
        request["approved_by"] = staff_id

        print(f"\nRequest [ID: {request_id}] approved by {staff_id}\n")

    def issue_card(self):
        if not self.requests:
            print("\nThere are no requests yet.\n")
            return

        print(
            "\n----- Issue Card -----\n"
        )

        request_id = input("\nRequest ID: ")

        if not request_id.strip():
            print("\nRequest ID cannot be empty.\n")
            return

        if request_id not in self.requests:
            print("\nInvalid request ID.\n")
            return
        
        request = self.requests[request_id]

        if request["status"] != "approved":
            print(f"\nRequest needs to be approved before cards can be issued.\n")
            return
        
        request["status"] = "issued"

        print(f"\nCard issued successfully.\n")

    def return_card(self):
        if not self.requests:
            print("\nThere are no requests yet.\n")
            return

        print(
            "\n----- Issue Card -----\n"
        )

        request_id = input("\nRequest ID: ")

        if not request_id.strip():
            print("\nRequest ID cannot be empty.\n")
            return

        if request_id not in self.requests:
            print("\nInvalid request ID.\n")
            return
        
        request = self.requests[request_id]   

        if request["status"] != "issued":
            print(f"\nCards need to be issued before they can be returned.\n")
            return
        
        request["status"] = "returned"

        print(f"\nCard successfully returned.\n")     
            

    def load(self):
        DB_DIR.mkdir(parents=True, exist_ok=True)

        try:
            with open(DB_FILE_PATH, "r") as file:
                self.requests = json.load(file)
        except FileNotFoundError:
            print(
                "\nNo requests database\n"
                "Creating a new database\n"
            )
        else:
            print("\nRequests loaded.")

    def save(self):
        try:
            with open(DB_FILE_PATH, "w") as file:
                json.dump(self.requests, file,  indent=4)
        except (FileNotFoundError, PermissionError):
            print("\nCouldn't save your session\n")
        else:
            print("\nSession saved\n")