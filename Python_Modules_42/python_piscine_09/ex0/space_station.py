from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):

    """
    Create a venv with pydantic installed.

    - python3 -m venv "name"
    - source "name"/bin/activate
    - pip install "pydantic>=2.0"

    This class inherits from Basemodel. It initialice and parse the entry
    given by using the function imported Field to check bad entries to the
    variables linked. The function tryes to change "bad entries"
    (said entries that) doesn't ajust to the given type, fixing some entry
    probems like chars to mark a date instead a int.
    """

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main():

    print("Space Station Data Validation")
    print("===============================")
    try:
        space_station = SpaceStation(station_id="ROKKO_001",
                                     name="International_Space_Station_ROKKO",
                                     crew_size=18,
                                     power_level=92.8,
                                     oxygen_level=77.3,
                                     last_maintenance="2026-02-12 17:17:45",
                                     is_operational=False,
                                     notes="Problem with Oxygen renovators."
                                     " Please send help.")

        print("Valid station created:")
        print("ID:", space_station.station_id)
        print("Name:", space_station.name)
        print("Crew:", space_station.crew_size)
        print("Power:", space_station.power_level)
        print("Oxygen:", space_station.oxygen_level)
        print("Last Maintenance:", space_station.last_maintenance)
        print("Status:", space_station.is_operational)
        print("Notes:", space_station.notes)

    except ValidationError as e:
        print("ROKKO_001 Data was corrupted.")
        for error in e.errors():
            field = error['loc']
            message = error['msg']
            print(f"Field {field}: ", message)

    print()
    print("===============================")
    print("Expected validation error:")

    try:
        corr_station = SpaceStation(station_id="ROKK###INSYAA_0100",
                                    name="IntNrnaional_Space_Statin_RK¬¬O",
                                    crew_size=0,
                                    power_level=1334.8,
                                    oxygen_level=7.777777,
                                    last_maintenance=datetime.now(),
                                    is_operational=13)
        print("Invalid station created:")
        print("ID:", corr_station.station_id)
        print("Name:", corr_station.name)
        print("Crew:", corr_station.crew_size)
        print("Power:", corr_station.power_level)
        print("Oxygen:", corr_station.oxygen_level)
        print("Last Maintenance:", corr_station.last_maintenance)
        print("Status:", corr_station.is_operational)
        print("Notes:", corr_station.notes)
    except ValidationError as e:
        print("ROKKO_001 Data was corrupted.")
        for error in e.errors():
            loc = "".join(str(x) for x in error['loc'])
            message = error['msg']
            print(f"{loc}: ", message)


if __name__ == "__main__":
    main()
