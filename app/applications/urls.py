from flask_smorest import Blueprint, abort
from flask.views import MethodView

from .schemas import ApplicationSchema
from app.schemas import DeleteMessageSchema


blp = Blueprint("Application", __name__)


@blp.route("/")
class ApplicationResource(MethodView):
    @blp.response(200, ApplicationSchema(many=True))
    def get(self):
        """Return list of applications"""
        pass

    @blp.arguments(ApplicationSchema)
    @blp.response(201, ApplicationSchema)
    def post(self, new_app):
        """Create a new application"""
        pass

    @blp.arguments(ApplicationSchema)
    @blp.response(200, ApplicationSchema)
    def put(self, updated_application, app_id):
        """Edit an existing application"""
        pass

    @blp.response(204, DeleteMessageSchema)
    def delete(self, app_id):
        """Delete an application"""
        pass
