import os
from pydantic import BaseSettings, AnyHttpUrl, EmailStr, validator
from typing import Optional, Dict, Any, List, Union

def get_secret(secret_name, default):
    try:
        with open('/run/secrets/{0}'.format(secret_name), 'r') as secret_file:
            return secret_file.read().strip()
    except IOError:
        return os.getenv(secret_name, default)

class ConfigClass(BaseSettings):

    SECRET_KEY: str = get_secret("SECRET_KEY", '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7')
    ALGORITHM: str = get_secret("ALGORITHM", 'HS256')

    ADMIN_KEY: str = get_secret("ADMIN_KEY", "BaseKey2021!")

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(get_secret("ACCESS_TOKEN_EXPIRE_MINUTES", 60 * 24 * 8))


    SQLALCHEMY_DATABASE_URL: str = get_secret("DATABASE_URL", 'postgresql://mvondofernando7777:jarodak47@localhost:5432/hotel')
    PREFERED_LANGUAGE: str = get_secret("PREFERED_LANGUAGE", 'fr')
    API_V1_STR: str = get_secret("EMAILS_FROM_NAME", "/api/v1")
    PROJECT_NAME: str = get_secret("EMAILS_FROM_NAME", "hotel api")

    # Minio config information
    MINIO_URL: str = get_secret("MINIO_URL", "files.develop.ouispeak.io")
    MINIO_KEY: str = get_secret("MINIO_KEY", "WlsCK$gSM@7CTqTdc3hmx0jshEzsCK$gSM@7CTqTdc3hmxlfyBo=")
    MINIO_SECRET: str = get_secret("MINIO_SECRET", "jDe6SMqcANAkflmmfCFyfGXD0n0N7r9AE2oKXpLRRCFyfGXD0n0N7r9AEqZfHoskT/4pOht+n1jjogmfDa0kpxfiw==")
    MINIO_SECURE: bool = get_secret("MINIO_SECURE", True)
    MINIO_BUCKET :str = get_secret("MINIO_BUCKET", "develop")
    UPLOADED_FILE_DEST: str = get_secret("UPLOADED_FILE_DEST", "upload")


    # SMTP_TLS: bool =  get_secret("SMTP_TLS", False)
    # SMTP_PORT: Optional[int] =  int(get_secret("SMTP_PORT", 1025))
    # SMTP_HOST: Optional[str] =  get_secret("SMTP_HOST", "app.dev.code101.ca")
    # SMTP_USER: Optional[str] =  get_secret("SMTP_USER", None)
    # SMTP_PASSWORD: Optional[str] =  get_secret("SMTP_PASSWORD", None)
    # EMAILS_FROM_EMAIL: Optional[EmailStr] =  get_secret("EMAILS_FROM_EMAIL", "no-reply@base.app")
    # EMAILS_FROM_NAME: Optional[str] =  get_secret("EMAILS_FROM_NAME", "Base App")

    # SMTP_TLS: bool =  get_secret("SMTP_TLS", False)
    # SMTP_PORT: Optional[int] =  int(get_secret("SMTP_PORT", 1025))
    # SMTP_HOST: Optional[str] =  get_secret("SMTP_HOST", "api.develop.ouispeak.io")
    # SMTP_USER: Optional[str] =  get_secret("SMTP_USER", None)
    # SMTP_PASSWORD: Optional[str] =  get_secret("SMTP_PASSWORD", None)
    # EMAILS_FROM_EMAIL: Optional[EmailStr] =  get_secret("EMAILS_FROM_EMAIL", "no-reply@ouispeak.io")
    # EMAILS_FROM_NAME: Optional[str] =  get_secret("EMAILS_FROM_NAME", "GeskMark App")

    SMTP_TLS: bool =  get_secret("SMTP_TLS", False)
    SMTP_SSL: bool =  get_secret("SMTP_SSL", False)
    SMTP_ASCII_ATTACHMENTS: bool =  get_secret("SMTP_ASCII_ATTACHMENTS", True)
    SMTP_PORT: Optional[int] =  int(get_secret("SMTP_PORT", 25))
    SMTP_HOST: Optional[str] =  get_secret("SMTP_HOST", "mail.kevmax.com")
    SMTP_USER: Optional[str] =  get_secret("SMTP_USER","freelance@kevmax.com")
    SMTP_PASSWORD: Optional[str] =  get_secret("SMTP_PASSWORD", "pLq44s@f43")
    EMAILS_FROM_EMAIL: Optional[EmailStr] =  get_secret("EMAILS_FROM_EMAIL", "Kevmax GestMark <freelance@kevmax.com>")
    EMAILS_FROM_NAME: Optional[str] =  get_secret("EMAILS_FROM_NAME", "App")


    @validator("EMAILS_FROM_NAME")
    def get_project_name(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if not v:
            return values["PROJECT_NAME"]
        return v

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = int(get_secret("EMAIL_RESET_TOKEN_EXPIRE_HOURS", 48))
    EMAILS_ENABLED: bool = get_secret("EMAILS_ENABLED", True) in ["True", True]
    EMAIL_TEMPLATES_DIR: str = "{}/app/main/templates/emails/render".format(os.getcwd())

    @validator("EMAILS_ENABLED", pre=True)
    def get_emails_enabled(cls, v: bool, values: Dict[str, Any]) -> bool:
        return bool(
            values.get("SMTP_HOST")
            and values.get("SMTP_PORT")
            and values.get("EMAILS_FROM_EMAIL")
        )

    EMAIL_TEST_USER: EmailStr = get_secret("EMAIL_TEST_USER","support@kevmax.com")
    FIRST_SUPERUSER: EmailStr = get_secret("FIRST_SUPERUSER","kevin.wamba@kevmax.com")
    FIRST_SUPERUSER_PASSWORD: str = get_secret("FIRST_SUPERUSER_PASSWORD","test")
    FIRST_SUPERUSER_FIRST_NAME: str = get_secret("FIRST_SUPERUSER_FIRST_NAME","Kevin")
    FIRST_SUPERUSER_LASTNAME: str = get_secret("FIRST_SUPERUSER_LASTNAME","WAMBA")
    USERS_OPEN_REGISTRATION: bool = get_secret("USERS_OPEN_REGISTRATION", False) in ["True", True]


    CELERY_BROKER_URL: str = get_secret("CELERY_BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND: str = get_secret("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")


    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "https://www.base.kevmax.com"
    ]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
        

    class Config:
        case_sensitive = True
    # UPLOADED_FILE_DEST = "test"
    # MINIO_BUCKET = "test"
Config = ConfigClass()