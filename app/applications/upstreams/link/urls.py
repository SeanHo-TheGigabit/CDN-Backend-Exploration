from flask_smorest import Blueprint, abort
from flask.views import MethodView

from ..schemas import UpstreamSchema
from app.schemas import DeleteMessageSchema

blp = Blueprint("UpstreamLink", __name__)


@blp.route("/<app_id>/upstream/link")
class UpstreamLinkResource(MethodView):
    @blp.response(200, UpstreamSchema)
    def get(self, app_id):
        """Return a linking upstreams"""
        pass

    @blp.arguments(UpstreamSchema)
    @blp.response(201, UpstreamSchema)
    def post(self, new_upstream, app_id):
        """Create a new upstream and link to the application"""
        pass

    @blp.arguments(UpstreamSchema)
    @blp.response(200, UpstreamSchema)
    def put(self, updated_upstream, app_id):
        """Edit an existing upstream linking"""
        pass

    @blp.response(204, DeleteMessageSchema)
    def delete(self, app_id):
        """Delete a linkinf with upstream"""
        pass
