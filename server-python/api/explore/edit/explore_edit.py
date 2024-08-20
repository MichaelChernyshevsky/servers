from flask import  jsonify
from flasgger import swag_from
from flask import Blueprint


@swag_from('../../../templates/swager/explore_edit.yaml')
def _explore_edit():
    return jsonify({'success':True})

explore_edit_bp = Blueprint('explore_edit_bp', __name__)
explore_edit_bp.add_url_rule("/explore", view_func=_explore_edit, methods=["PATCH"])