from flask import jsonify
from flasgger import swag_from
from flask import Blueprint

@swag_from('../../../templates/swager/explore_create.yaml')
def _explore_create():
    return jsonify({'success':True})

explore_create_bp = Blueprint('explore_create_bp', __name__)
explore_create_bp.add_url_rule("/explore", view_func=_explore_create, methods=["POST"])