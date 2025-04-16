# generated by fastapi-codegen:
#   filename:  discriminator_in_root_with_properties.yaml
#   timestamp: 2020-06-19T00:00:00+00:00

from __future__ import annotations

from typing import Literal, Optional, Union

from pydantic import BaseModel, Extra, Field


class IssueContextVariable(BaseModel):
    id: Optional[int] = Field(None, description='The issue ID.')
    key: Optional[str] = Field(None, description='The issue key.')
    type: str = Field(..., description='Type of custom context variable.')


class UserContextVariable(BaseModel):
    accountId: str = Field(..., description='The account ID of the user.')
    type: str = Field(..., description='Type of custom context variable.')


class CustomContextVariable1(UserContextVariable):
    class Config:
        extra = Extra.forbid

    type: Literal['user'] = Field(..., description='Type of custom context variable.')


class CustomContextVariable2(IssueContextVariable):
    class Config:
        extra = Extra.forbid

    type: Literal['issue'] = Field(..., description='Type of custom context variable.')


class CustomContextVariable(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Union[CustomContextVariable1, CustomContextVariable2] = Field(
        ..., discriminator='type'
    )
