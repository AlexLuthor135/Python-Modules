from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field()
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field()
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode='after')
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID is not valid")
        if not any(
            m.rank in [Rank.CAPTAIN, Rank.COMMANDER] for m in self.crew
        ):
            raise ValueError("No high ranking officer in the crew")
        if self.duration_days > 365:
            exp: int = sum(m.years_experience >= 5 for m in self.crew)
            if exp < len(self.crew) / 2:
                raise ValueError("Crew has too low experience")
        if not all(m.is_active for m in self.crew):
            raise ValueError("Crew has inactive members")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    commander = CrewMember(
        member_id="CR001",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=45,
        specialization="Mission Command",
        years_experience=15,
    )
    lieutenant = CrewMember(
        member_id="CR002",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=32,
        specialization="Navigation",
        years_experience=7,
    )
    officer = CrewMember(
        member_id="CR003",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=28,
        specialization="Engineering",
        years_experience=3,
    )
    mission = SpaceMission(
        mission_id="M2026_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2027, 3, 1),
        duration_days=900,
        crew=[commander, lieutenant, officer],
        budget_millions=2500.0,
    )
    print("Valid mission created:")
    print("Mission:", mission.mission_name)
    print("ID:", mission.mission_id)
    print("Destination:", mission.destination)
    print("Duration:", mission.duration_days, "days")
    print(f"Budget: ${mission.budget_millions}M")
    print("Crew size:", len(mission.crew))
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value})"
            f" - {member.specialization}"
        )
    print("\n=========================================")
    try:
        SpaceMission(
            mission_id="M2026_TEST",
            mission_name="Test Mission",
            destination="Mars",
            launch_date=datetime(2027, 3, 1),
            duration_days=900,
            crew=[lieutenant, officer],
            budget_millions=1000.0,
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()
