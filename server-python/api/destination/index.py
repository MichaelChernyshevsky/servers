

from flask import Blueprint, request
from flasgger import swag_from

from model.Contact import Contact
from model.Destination import Destination

@swag_from('../../swagger/destination_get.yaml')
def get_destinations():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', default=10, type=int)
    query = Destination.query.paginate(page=page, per_page=limit)
    items = []
    for destination in query.items:
        items.append(destination.serialize())

    return {
       "data": items,
       "total": query.total,
    }

@swag_from('../../swagger/destination_get_contacts.yaml')
def get_destination_contacts(destination_id):
    # destination_id = request.args.get('destination_id', type=int)
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', default=10, type=int)
    print(destination_id)
    query = Contact.query.filter_by(destination_id=destination_id).paginate(page=page, per_page=limit)
    items = []
    for contact in query:
        items.append(contact.serialize())
    return { "data": items
            , "total": query.total
            }
destination_bp = Blueprint('destination_bp', __name__)
destination_bp.add_url_rule("/destination", view_func=get_destinations, methods=["GET"])
destination_bp.add_url_rule("/destination/<int:destination_id>/contacts", view_func=get_destination_contacts, methods=["GET"])