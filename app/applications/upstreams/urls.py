from flask_smorest import Blueprint, abort
from flask import request
from flask.views import MethodView

from .schemas import UpstreamSchema
from app.schemas import DateFilterQuerySchema, DeleteMessageSchema

blp = Blueprint("Upstream", __name__)


class GetQueryArgs(DateFilterQuerySchema):
    pass


@blp.route("/<app_id>/upstream")
class UpstreamResource(MethodView):
    @blp.arguments(GetQueryArgs, location="query")
    @blp.response(200, UpstreamSchema(many=True))
    @blp.paginate()
    def get(self, query_args, pagination_parameters, app_id):
        """Return list of upstreams"""
        pagination_parameters.item_count = 100
        print("Query args: ", query_args)
        print(
            {
                "app_id": app_id,
                "first_item": pagination_parameters.first_item,
                "last_item": pagination_parameters.last_item,
            }
        )

    @blp.arguments(UpstreamSchema)
    @blp.response(201, UpstreamSchema)
    def post(self, new_upstream, app_id):
        """Create a new upstream"""
        pass

    @blp.arguments(UpstreamSchema)
    @blp.response(200, UpstreamSchema)
    def put(self, updated_upstream, app_id):
        """Edit an existing upstream"""
        pass

    @blp.response(204, DeleteMessageSchema)
    def delete(self, app_id):
        """Delete an upstream"""
        pass
