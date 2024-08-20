from flask import jsonify
from flasgger import swag_from
from flask import Blueprint

@swag_from('../../../templates/swager/explore_get.yaml')
def _explore_get():
    return jsonify({'success':True})
    

explore_get_bp = Blueprint('explore_get_bp', __name__)
explore_get_bp.add_url_rule("/explore", view_func=_explore_get, methods=["GET"])