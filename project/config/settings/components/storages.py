from os import environ
from typing import Any

from decouple import config

DATABASES: dict[str, Any] = {
    "default": {
        "ENGINE": config("DB_ENGINE", cast=str),
        "NAME": config("POSTGRES_DB", cast=str),
        "USER": config("POSTGRES_USER", cast=str),
        "PASSWORD": config("POSTGRES_PASSWORD", cast=str),
        "HOST": config("POSTGRES_HOST", cast=str),
        "PORT": config("POSTGRES_PORT", cast=int),
    }
}
CHANNEL_LAYERS: dict[str, Any] = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(config("REDIS_HOST", cast=str), config("REDIS_PORT", cast=int))],
        },
    },
}


MINIO_ENDPOINT: str = config("FILE_STORAGE_ENDPOINT", cast=str)
DEFAULT_FILE_STORAGE: str = config("FILE_STORAGE", cast=str)
MINIO_MEDIA_FILES_BUCKET: str = config("FILE_STORAGE_MEDIA_BUCKET_NAME", cast=str)
MINIO_USE_HTTPS: bool = config("FILE_STORAGE_USE_HTTPS", cast=bool)
MINIO_CONSISTENCY_CHECK_ON_START: bool = False
MINIO_BUCKET_CHECK_ON_SAVE: bool = True
MINIO_ACCESS_KEY: str = config("MINIO_ROOT_USER", cast=str)
MINIO_SECRET_KEY: str = config("MINIO_ROOT_PASSWORD", cast=str)
MINIO_PUBLIC_BUCKETS: list[str] = [config("FILE_STORAGE_MEDIA_BUCKET_NAME", cast=str)]
MINIO_IMAGES_HOST = config("MINIO_IMAGES_HOST", cast=str)