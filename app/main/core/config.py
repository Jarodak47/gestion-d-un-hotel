import os

from pydantic import BaseSettings

class ConfigClass(BaseSettings):

    def get_secret(secret_name, default):
        try:
            with open('/run/secrets/{0}'.format(secret_name), 'r') as secret_file:
                return secret_file.read().strip()
        except IOError:
            return os.getenv(secret_name, default)


    mysql_url: str = get_secret("DATABASE_URL", 'postgresql://postgres:postgres@127.0.0.1:5433/test_fastapi')
    PREFERED_LANGUAGE: str = get_secret("PREFERED_LANGUAGE", 'fr')

    API_V1_STR: str = get_secret("EMAILS_FROM_NAME", "/api/v1")
    PROJECT_NAME: str = get_secret("EMAILS_FROM_NAME", "projet stage api")