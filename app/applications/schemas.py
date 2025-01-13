from marshmallow import Schema, fields, validate

class ApplicationSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
