from pathlib import Path


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_TITLE = "Flask Smorest API"
    API_VERSION = "v1"
    API_SPEC = Path(__file__).parent / "api_spec.yaml"  # Path to API specification file
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/docs"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    DEBUG = True  # Set to False in production

    UPLOAD_FOLDER = Path(__file__).parent / "uploads"
