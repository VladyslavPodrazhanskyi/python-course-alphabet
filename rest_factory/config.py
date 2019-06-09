import os

class Config:
    DB_CONNECTION = "psql..//"
    Default = "default"

class DevConfig(Config):
    DB_CONNECTION = "DEVpsql..//"

class TestConfig(Config):
    DB_CONNECTION = "TESTpsql..//"

def run_config():
    env = os.environ.get("ENV")
    if env == "DEV":
        return DevConfig
    elif env == "TEST":
        return TestConfig
    else:
        return Config