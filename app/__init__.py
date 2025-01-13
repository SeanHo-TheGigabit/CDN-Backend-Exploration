class RegisterAppResources:
    @staticmethod
    def register_resources(app):
        URL_PREFIX = "/api/app"
        # fmt:off
        from app.applications.urls import blp as app_url
        app.register_blueprint(app_url, url_prefix=URL_PREFIX)

        from app.applications.upstreams.urls import blp as upstream_url
        app.register_blueprint(upstream_url, url_prefix=URL_PREFIX)

        from app.applications.rules.urls import blp as rule_url
        app.register_blueprint(rule_url, url_prefix=URL_PREFIX)
        # fmt:on

        return app
