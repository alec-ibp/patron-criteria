import os
import importlib
from typing import Any
from functools import lru_cache


class ServiceSettings:
    _SETTINGS_MODULE: str = os.environ.get('PROJ_SETTINGS_MODULE', 'config.service_settings')

    def __init__(self) -> None:
        module: str = importlib.import_module(self._SETTINGS_MODULE)

        tuple_settings: tuple[str] = (
            "ALLOWED_HOSTS",
            "INSTALLED_APPS",
            "CORS_ALLOWED_HOSTS",
            "CORS_ALLOWED_METHODS",
            "CORS_ALLOWED_HEADERS",  # TODO CHECK MORE ABOUT CORS
        )

        self._explicit_settings: set[str] = set()
        for setting in dir(module):
            if setting.isupper():
                setting_value: Any = getattr(module, setting)
                if setting in tuple_settings and not isinstance(setting_value, (tuple, list)):
                    raise ValueError(f"Setting {setting} must be a tuple or list")
                setattr(self, setting, getattr(module, setting))
                self._explicit_settings.add(setting)


@lru_cache
def get_service_settings() -> ServiceSettings:
    return ServiceSettings()


settings: ServiceSettings = get_service_settings()
