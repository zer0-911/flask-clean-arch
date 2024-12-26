from app.repositories.userRepository import UserRepository
from flask_bcrypt import Bcrypt

class UserService:
    def __init__(self, bcrypt: Bcrypt):
        self.bcrypt = bcrypt

    def get_user_by_id(self, user_id):
        return UserRepository.get_by_id(user_id)

    def create_user(self, username, email, password):
        hashed_password = self.bcrypt.generate_password_hash(password).decode('utf-8')
        return UserRepository.add_user(username, email, hashed_password)

    def update_user(self, user_id, **kwargs):
        if 'password' in kwargs:
            kwargs['password'] = self.bcrypt.generate_password_hash(kwargs['password']).decode('utf-8')
        return UserRepository.update_user(user_id, **kwargs)

    def delete_user(self, user_id):
        return UserRepository.delete_user(user_id)
