# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T11:23:26+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, RootModel, constr


class Boolean(RootModel[bool]):
    root: bool


class Double(RootModel[float]):
    root: float


class ErrorMessage(RootModel[str]):
    root: str


class FilterValue(RootModel[str]):
    root: str


class FilterValueList(RootModel[List[FilterValue]]):
    root: List[FilterValue] = Field(..., min_length=1)


class GetEntitlementFilterName(Enum):
    CUSTOMER_IDENTIFIER = 'CUSTOMER_IDENTIFIER'
    DIMENSION = 'DIMENSION'


class GetEntitlementFilters(RootModel[Optional[Dict[str, FilterValueList]]]):
    root: Optional[Dict[str, FilterValueList]] = None


class Integer(RootModel[int]):
    root: int


class InternalServiceErrorException(BaseModel):
    message: Optional[ErrorMessage] = None


class InvalidParameterException(BaseModel):
    message: Optional[ErrorMessage] = None


class NonEmptyString(RootModel[constr(pattern=r'\S+')]):
    root: constr(pattern=r'\S+')


class ProductCode(RootModel[constr(min_length=1, max_length=255)]):
    root: constr(min_length=1, max_length=255)


class String(RootModel[str]):
    root: str


class ThrottlingException(BaseModel):
    message: Optional[ErrorMessage] = None


class Timestamp(RootModel[datetime]):
    root: datetime


class XAmzTarget(Enum):
    AWSMPEntitlementService_GetEntitlements = 'AWSMPEntitlementService.GetEntitlements'


class EntitlementValue(BaseModel):
    BooleanValue: Optional[Boolean] = None
    DoubleValue: Optional[Double] = None
    IntegerValue: Optional[Integer] = None
    StringValue: Optional[String] = None


class GetEntitlementsRequest(BaseModel):
    Filter: Optional[GetEntitlementFilters] = None
    MaxResults: Optional[Integer] = None
    NextToken: Optional[NonEmptyString] = None
    ProductCode_1: ProductCode = Field(..., alias='ProductCode')


class Entitlement(BaseModel):
    CustomerIdentifier: Optional[NonEmptyString] = None
    Dimension: Optional[NonEmptyString] = None
    ExpirationDate: Optional[Timestamp] = None
    ProductCode_1: Optional[ProductCode] = Field(None, alias='ProductCode')
    Value: Optional[EntitlementValue] = None


class EntitlementList(RootModel[List[Entitlement]]):
    root: List[Entitlement] = Field(..., min_length=0)


class GetEntitlementsResult(BaseModel):
    Entitlements: Optional[EntitlementList] = None
    NextToken: Optional[NonEmptyString] = None
