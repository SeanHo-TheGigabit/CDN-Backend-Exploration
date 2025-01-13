from marshmallow import Schema, fields, validate


class ServerSchema(Schema):
    ip = fields.Str(required=True)
    port = fields.Int(required=True)


class UpstreamSchema(Schema):
    id = fields.Int(dump_only=True)
    app_id = fields.Int(required=True)
    name = fields.Str(required=True)
    node = fields.Nested(ServerSchema, required=True)
    ssl = fields.Bool(required=True)
    disable_ssl_verify = fields.Bool(required=True)
