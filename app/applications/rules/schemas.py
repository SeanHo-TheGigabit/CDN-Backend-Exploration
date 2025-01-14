from marshmallow import Schema, fields, validate


class ActionSchema(Schema):
    id = fields.Int(required=True)
    type = fields.Str(required=True)
    set_req_header = fields.Dict(keys=fields.Str(), values=fields.Str())


class CacheKeySchema(Schema):
    name = fields.Str(required=True)
    id = fields.Int(required=True)
    args = fields.Str(missing="")


class CacheSchema(Schema):
    enable_global = fields.Boolean(required=True)
    disable_convert_head = fields.Boolean(required=True)
    cluster_hash = fields.Boolean(required=True)
    enforce_cache = fields.Boolean(required=True)
    cache_key = fields.List(fields.Nested(CacheKeySchema), required=True)


class StickySchema(Schema):
    key = fields.Str(required=True)
    enable = fields.Boolean(required=True)
    ttl = fields.Int(required=True)
    level = fields.Str(required=True)
    mode = fields.Str(required=True)


class ProxySchema(Schema):
    read_timeout_unit = fields.Str(required=True)
    backup_upstream = fields.List(
        fields.Dict(keys=fields.Str(), values=fields.Int()), required=True
    )
    upstream_el_code = fields.Str(required=True)
    connect_timeout = fields.Int(required=True)
    balancer = fields.Dict(keys=fields.Str(), values=fields.Str(), required=True)
    send_timeout = fields.Int(required=True)
    connect_timeout_unit = fields.Str(required=True)
    retry_condition = fields.List(fields.Str(), required=True)
    send_timeout_unit = fields.Str(required=True)
    read_timeout = fields.Int(required=True)
    upstream = fields.List(
        fields.Dict(keys=fields.Str(), values=fields.Int()), required=True
    )
    grpc = fields.Boolean(required=True)
    sticky = fields.Nested(StickySchema, required=True)
    retries = fields.Int(required=True)


class ConditionValueSchema(Schema):
    val = fields.Str(required=True)
    type = fields.Str(required=True)
    id = fields.Int(required=True)


class ConditionSchema(Schema):
    id = fields.Int(required=True)
    variable = fields.Dict(keys=fields.Str(), values=fields.Str(), required=True)
    operator = fields.Dict(keys=fields.Str(), values=fields.Str(), required=True)
    values = fields.List(fields.Nested(ConditionValueSchema), required=True)


class WafSchema(Schema):
    resp_body_size = fields.Int(required=True)
    rule_sets = fields.List(fields.Int(), required=True)
    cross_requests = fields.Boolean(required=True)
    action = fields.Str(required=True)
    page_template_status_code = fields.Int(required=True)
    clearance_time = fields.Int(required=True)


class RuleSchema(Schema):
    id = fields.Int(dump_only=True)
    enable_rule = fields.Boolean(default=True)
    order = fields.Int(required=True)
    top = fields.Boolean(default=False)
    last = fields.Boolean(default=False)
    waf = fields.Nested(WafSchema, required=True)
    comment = fields.Str(required=True)
    cache = fields.Nested(CacheSchema, required=True)
    _modified_unix = fields.Float(required=True)
    _created_unix = fields.Float(required=True)
    actions = fields.List(fields.Nested(ActionSchema), required=True)
    proxy = fields.Nested(ProxySchema, required=True)
    conditions = fields.List(fields.Nested(ConditionSchema), required=True)


class RuleOrderSchema(Schema):
    rule_id = fields.Int(required=True)
    order = fields.Int(required=True)
