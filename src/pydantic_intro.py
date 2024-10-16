from datetime import datetime
from pydantic import BaseModel
from typing import Annotated


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"


if __name__ == "__main__":
    external_data = {
        "id": "123",
        "signup_ts": "2017-06-01 12:22",
        "friends": [1, "2", b"3"],
    }
    user = User(**external_data)
    print(user)
    # > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
    print(user.id)
    # > 123
