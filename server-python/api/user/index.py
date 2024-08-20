from http import HTTPStatus
from flask import Blueprint, jsonify
from flasgger import swag_from

@swag_from('../../swagger/user_change_destination.yaml')
def change_destination():
    return jsonify({'success':True}), HTTPStatus.OK

@swag_from('../../swagger/user_edit.yaml')
def update_user_info():
    return jsonify({'success':True}), HTTPStatus.OK

@swag_from('../../swagger/user_update_image.yaml')
def update_user_image():
    return 

@swag_from('../../swagger/user_delete.yaml')
def delete_user():
    return jsonify({'success':True})

@swag_from('../../swagger/user_get.yaml')
def get_user_info():
    return jsonify({'success':True}), HTTPStatus.OK

user_bp = Blueprint('user_bp', __name__)
user_bp.add_url_rule("/user", view_func=update_user_info, methods=["POST"])
user_bp.add_url_rule("/user", view_func=delete_user, methods=["DELETE"])
user_bp.add_url_rule("/user/destination", view_func=change_destination, methods=["POST"])
user_bp.add_url_rule("/user/profile_image", view_func=update_user_image, methods=["POST"])