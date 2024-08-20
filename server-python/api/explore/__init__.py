# explore
from api.explore.create.explore_create import explore_create_bp
from api.explore.delete.explore_delete import explore_delete_bp
from api.explore.get.explore_get import explore_get_bp
from api.explore.edit.explore_edit import explore_edit_bp




def register_explore(app):
    app.register_blueprint(explore_delete_bp)
    app.register_blueprint(explore_edit_bp)
    app.register_blueprint(explore_get_bp)