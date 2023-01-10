import os
import logging
from typing import Union


class ConfigException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def get_or_throw(key: str) -> str:
    value = os.environ.get(key)
    if value is None:
        raise ConfigException(f"Missing config for [{key}]")
    return value


def get_logging_level() -> Union[str, int]:
    return os.environ.get("LOG_LEVEL") or logging.INFO


def get_code() -> str:
    return get_or_throw("CODE")


def get_client_id() -> str:
    return get_or_throw("CLIENT_ID")


def get_expiration_range() -> str:
    return os.environ.get("EXPIRATION_RANGE") or "90"


def get_strike_count() -> str:
    return os.environ.get("STRIKE_COUNT") or "75"


def get_ddb_option_table() -> str:
    return get_or_throw("DDB_QUOTE_TABLE")


def get_ddb_underlying_table() -> str:
    return get_or_throw("DDB_UNDERLYING_TABLE")
