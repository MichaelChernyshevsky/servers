from flask import jsonify
from flasgger import swag_from
from flask import Blueprint


@swag_from('../../../templates/swager/explore_delete.yaml')
def _explore_delete():
    return jsonify({'success':True})

explore_delete_bp = Blueprint('explore_delete_bp', __name__)
explore_delete_bp.add_url_rule("/explore", view_func=_explore_delete, methods=["DELETE"])