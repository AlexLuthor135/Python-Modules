from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field()
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_contact(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with AC")
        if self.contact_type == ContactType.PHYSICAL:
            if not self.is_verified:
                raise ValueError("Physical contact must be verified")
        if self.contact_type == ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError("Telepathic contact requires 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Signal confirmation invalid")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2026, 10, 18),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )
        print("Valid contact report:")
        print("ID:", contact.contact_id)
        print("Type:", contact.contact_type.value)
        print("Location:", contact.location)
        print(f"Signal: {contact.signal_strength}/10")
        print("Duration:", contact.duration_minutes, "minutes")
        print("Witnesses:", contact.witness_count)
        print("Message:", contact.message_received)
        print("\n======================================")
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2026, 10, 18),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=1,
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()
