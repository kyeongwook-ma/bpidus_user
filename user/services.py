from .models import User


def create_user(_name: str, _nickname: str, _email: str, _phone_number: str) -> bool:
    User(name=_name, nickname=_nickname, email=_email, phone_number=_phone_number).save()
    return True