from typing import Dict
from app.schemas import UserInDB
from app.core.security import get_password_hash

fake_users_db: Dict[str, dict] = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        # A senha "secret" é armazenada com seu hash gerado pelo bcrypt
        "hashed_password": get_password_hash("secret"),
        "disabled": False,
    },
    "lucas": {
        "username": "lucas",
        "full_name": "lucas f",
        "email": "lucas@gmail.com",
        # A senha "123" é armazenada com seu hash gerado pelo bcrypt
        "hashed_password": get_password_hash("123"),
        "disabled": False,
    }
}
