from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):

    """
    Enum class just to check the quantity of contacts existent in the data
    check. Need enum to be fully accesible from outside the Class
    """

    physical = "physical"
    radio = "radio"
    visual = "visual"
    telepathic = "telepathic"


class AlienContact(BaseModel):

    """
    Added to the functionality of BaseModel, we can adjust our own check of
    the entries gived usin @model_validator. If can affect before or after
    the field validation to check some information. The comprobations right
    now goes.

    -Field -> chechs the imput values and types
    -@model_validator -> checks for static values in the data given

    If field checks some variable wrong, the workflow breaks on the setter,
    not giving the possibility to check in model_validator.
    """

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_recieved: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validator(self):

        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        elif (self.contact_type == ContactType.physical
              and not self.is_verified):
            raise ValueError("Physical contact reports must be verified")

        elif (self.contact_type == ContactType.telepathic
              and self.witness_count < 3):
            raise ValueError("Telepatic contact requires at least 3 witnesses")

        elif self.signal_strength > 7.0 and not self.message_recieved:
            raise ValueError("Strong signals must include a recieved message")

        return self


if __name__ == "__main__":

    print("Alien Contact Log Validation")

    data_of_contacts = [
        {
            "contact_id": "AC_2024_001",
            "timestamp": datetime.now(),
            "location": "Area 51, Nevada",
            "contact_type": "radio",
            "signal_strength": 8.5,
            "duration_minutes": 45,
            "witness_count": 5,
            "message_recieved": "Greetings from Zeta Reticuli",
            "is_verified": True
        },
        {
            "contact_id": "2024_002",
            "timestamp": datetime.now(),
            "location": "Hokaido, Jappan",
            "contact_type": "telepatic",
            "signal_strength": 12.5,
            "duration_minutes": 22,
            "witness_count": 6,
            "is_verified": False
        },
        {
            "contact_id": "AC_2024_003",
            "timestamp": datetime.now(),
            "location": "Palacio de la Moncloa, Madrid",
            "contact_type": "physical",
            "signal_strength": 10.0,
            "duration_minutes": 165,
            "witness_count": 1,
            "message_recieved": "We came to destroy your politicians",
            "is_verified": True
        },
        {
            "contact_id": "AC_2024_003",
            "timestamp": datetime.now(),
            "location": "Palacio de la Moncloa, Madrid",
            "contact_type": "physical",
            "signal_strength": 10.0,
            "duration_minutes": 165,
            "witness_count": 1,
            "is_verified": True
        },
        {
            "contact_id": "AC_2024_003",
            "timestamp": datetime.now(),
            "location": "Pa",
            "contact_type": "physical",
            "signal_strength": 10.0,
            "duration_minutes": 165,
            "witness_count": 1,
            "is_verified": False
        }
    ]

    for data in data_of_contacts:
        try:

            contact = AlienContact(**data)

            print("=================================")
            print("Valid contact report:")
            print("ID:", contact.contact_id)
            print("Type:", contact.contact_type._name_)
            print("Location:", contact.location)
            print(f"Signal: {contact.signal_strength}/10")
            print(f"Duration:{contact.duration_minutes} minutes")
            print("Witnesses:", contact.witness_count)
            if contact.message_recieved is not None:
                print("Message:", contact.message_recieved)
            print()

        except ValidationError as e:
            print("=================================")
            print("Expected validation error:")
            print("Contact:", data['contact_id'])
            for error in e.errors():
                loc = "".join(str(x) for x in error['loc'])
                if loc == "":
                    loc = "message"
                message = error['msg']
                print(f"{loc}: ", message)

        print()
