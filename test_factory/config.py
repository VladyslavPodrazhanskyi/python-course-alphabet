import os

class Config:
    DEFAULT = "default value"
    TEST_DB_CONNECTION = "psql..//"


class DevConfig(Config):
    TEST_DB_CONNECTION = "DEV_psql..//"


class TestConfig(Config):
    TEST_DB_CONNECTION = "TEST_psql..//"


def run_config():
    env = os.environ.get("ENV")
    if env == "DEV":
        return DevConfig
    elif env == "TEST":
        return TestConfig
    else:
        return Config
