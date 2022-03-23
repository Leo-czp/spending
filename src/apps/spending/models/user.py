from typing import List

from extension.mysql_client import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String(32), nullable=True)
    name = db.Column(db.String(50), nullable=True, primary_key=True)
    password = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(20), nullable=True)

    @classmethod
    def login(cls, name: str, password: str) -> bool:
        user = cls.query.filter_by(name=name, password=password).first()
        return bool(user)

    @classmethod
    def emails(cls) -> List[str]:
        return [user.email for user in cls.query.all()]

    @classmethod
    def names(cls) -> List[str]:
        return [user.name for user in cls.query.all()]
