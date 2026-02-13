from enum import Enum
from pydantic import BaseModel, ValidationError, model_validator, Field
from datetime import datetime
import json


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):

    """
    The crew memebers are created first so if one of them is bad setted the
    workflow breaks here.
    """
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):

    """
    We can make BaseModel comprobation nested. It works the same way it as
    any simple validation. Each stage is separated, so if it breaks in one of
    them it doesnt continue to the next one.
    """

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self):

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(member.rank in {Rank.captain, Rank.commander}
                   for member in self.crew):
            raise ValueError("There is not a captain or commander"
                             " in the mission")

        if self.duration_days > 365:
            experienced = []
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced.append(member)

            if len(experienced) < len(self.crew) / 2:
                raise ValueError("The crew is not experienced enough")

        if any(not member.is_active for member in self.crew):
            raise ValueError("There is at least a non-active crew member")

        return self


if __name__ == "__main__":

    with open("ex2/space_missions.json", "r") as file:
        data = json.load(file)

    print("Space Mission Crew Validation")

    for mission_data in data:
        try:
            mission = SpaceMission(**mission_data)

            print("======================================")
            print("Valid mission created:")
            print("Mission:", mission.mission_name)
            print("ID:", mission.mission_id)
            print("Destination:", mission.destination)
            print(f"Duration: {mission.duration_days} days")
            print(f"Budget: {mission.budget_millions}M")
            print("Crew Size:", len(mission.crew))
            print("Crew Members:")
            for member in mission.crew:
                print(f" - {member.name} ({member.rank._name_})"
                      f" - {member.specialization}")

            print()
        except ValidationError as e:
            print("=================================")
            print("Expected validation error:")
            for error in e.errors():
                loc = "".join(str(x) for x in error['loc'])
                message = error['msg']
                print(f"{loc}: ", message)

        print()
