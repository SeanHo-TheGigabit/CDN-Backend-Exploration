from marshmallow import Schema, fields, validate


class DateFilterQuerySchema(Schema):
    start = fields.String()
    end = fields.String()
    q = fields.String()
    order = fields.String(validate=validate.OneOf(['asc', 'desc']))

class DeleteMessageSchema(Schema):
    code = fields.Integer(required=True)
    message = fields.String(required=False)
