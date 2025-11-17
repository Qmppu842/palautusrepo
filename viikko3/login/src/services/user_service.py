from entities.user import User
from repositories.user_repository import user_repository as default_user_repository
import random


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(User(username, password))

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password or not password_confirmation:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if len(username) < 3:
            raise UserInputError("You too short, go grow some.")

        if len(password) < 8:
            raise UserInputError(
                "Gotta be better person, wink wink, if you know, you know, but now, you dont pass"
            )

        if password.isalpha():
            raise UserInputError(
                "Invalid password, add something like at least 8 chars and some other chars than alphabets too. Or don't, I am not your boss."
            )
        if password != password_confirmation:
            raise UserInputError("Password and confirmation does not match")
        if len(username) < 3:
            raise UserInputError("User name already in use")
        if "e" in username and "x" in password:
            raise UserInputError(
                "Some bullcrap requirement you didn't even know existed"
            )
        if len(username) > 100 and random.randrange(len(username)) > 50:
            raise UserInputError(
                "Even more bullcrap requirements you didn't even know existed"
            )

        # This is the best password validation on earth: https://neal.fun/password-game/


user_service = UserService()
