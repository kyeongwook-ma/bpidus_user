from .models import User


def create_user(_name: str, _nickname: str, _phone_number: str) -> bool:
    User(name=_name, nickname=_nickname, phone_number=_phone_number).save()
    return True


def get_user(_id) -> User:
    return User.objects.get(pk=_id)
