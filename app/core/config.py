from typing import Annotated, Any, Literal

from pydantic import (
    AnyUrl,
    BeforeValidator,
    computed_field,
)
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Self


def parse_cors(v: Any) -> list[str] | str: #This function is a utility to parse CORS origins, transforming a comma-separated string into a list or returning it as is if it's already a list. This helps ensure consistent handling of CORS configurations.
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(#This configuration tells Pydantic to load environment variables from a .env file located one level up from the current directory, to ignore empty variables, and to ignore extra fields not defined in the model.
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )
    ENVIRONMENT: Literal["local", "staging", "production"] = "local" #The deployment environment (local, staging, production).
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = [] #List of allowed origins for CORS, which can be specified as a string or a list.

    @computed_field  # type: ignore[prop-decorator]
    @property
    def ALL_CORS_ORIGINS(self) -> list[str]:
        return [str(origin).rstrip("/") for origin in self.BACKEND_CORS_ORIGINS]#This property returns a list of all allowed CORS origins

    PROJECT_NAME: str
    


settings = Settings()  # type: ignore