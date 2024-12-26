from flask import Blueprint, jsonify, request
from app.services.userService import UserService
from app import bcrypt

user_bp = Blueprint('user_bp', __name__)

def get_user_service():
    return UserService(bcrypt)

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user_service = get_user_service()
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'message': 'User not found'}), 404

@user_bp.route('/', methods=['POST'])
def create_user():
    user_service = get_user_service()
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Missing data'}), 400

    user = user_service.create_user(data['username'], data['email'], data['password'])
    return jsonify(user.to_dict()), 201

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_service = get_user_service()
    data = request.get_json()
    user = user_service.update_user(user_id, **data)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'message': 'User not found'}), 404

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_service = get_user_service()
    if user_service.delete_user(user_id):
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'message': 'User not found'}), 404
