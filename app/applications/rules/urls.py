from flask_smorest import Blueprint, abort
from flask.views import MethodView
from werkzeug.utils import secure_filename

from .schemas import RuleSchema, RuleOrderSchema
from app.schemas import DateFilterQuerySchema, DeleteMessageSchema

blp = Blueprint("Rules", __name__)


class GetQueryArgs(DateFilterQuerySchema):
    pass


@blp.route("/<app_id>/rule")
class RulesResource(MethodView):
    @blp.arguments(GetQueryArgs, location="query")
    @blp.response(200, RuleSchema(many=True))
    @blp.paginate()
    def get(self, query_args, pagination_parameters, app_id):
        """Return list of rules"""
        pagination_parameters.item_count = 100
        print("Query args: ", query_args)
        print(
            {
                "app_id": app_id,
                "first_item": pagination_parameters.first_item,
                "last_item": pagination_parameters.last_item,
            }
        )

    @blp.arguments(RuleSchema, location="json")
    @blp.response(
        201,
        RuleSchema,
    )
    def post(self, new_rule, app_id):
        """Create a new rule"""
        # base_dir = "/path/to/storage/dir/"
        # file_1 = new_rule["file_1"]
        # file_1.save(os.path.join(base_dir, secure_filename(file_1.filename)))
        pass

    @blp.arguments(RuleSchema, location="json")
    @blp.response(200, RuleSchema)
    def put(self, updated_rule, app_id):
        """Edit an existing rule"""
        pass

    @blp.response(204, DeleteMessageSchema)
    def delete(self, app_id):
        """Delete a rule"""
        pass


@blp.route("/<app_id>/rule/reorder")
class RulesReorderResource(MethodView):
    @blp.arguments(RuleOrderSchema(many=True), location="json")
    @blp.response(200, RuleOrderSchema(many=True))
    def post(self, rules_order, app_id):
        """Reorder rules - For reorder button"""
        pass
