from marshmallow import Schema, fields, validate
from flask_smorest.fields import Upload


class RuleSchema(Schema):
    id = fields.Int(dump_only=True)
    data = fields.Dict()
    order = fields.Int()
