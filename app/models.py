from typing import Dict
from app.schemas import UserInDB

fake_users_db: Dict[str, dict] = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",  # "fakehash" + "secret"
        "disabled": False,
    }
}
