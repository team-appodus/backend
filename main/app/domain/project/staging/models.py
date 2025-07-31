from typing import List, Optional

from appodus_utils import BaseEntity, PageRequest, BaseQueryDto, Object
from pydantic import Field, EmailStr
from sqlalchemy import Column, String, JSON, Boolean, Text, Integer


class ProjectStaging(BaseEntity):
    __tablename__ = 'projects_staging'
    fullname = Column(String(100), nullable=False)
    email = Column(String(60), nullable=False)
    phone = Column(String(17), nullable=False)
    company_name = Column(String(100), nullable=False)
    budget = Column(String(100), nullable=True)
    timeline = Column(String(100), nullable=True)
    what_building = Column(Text, nullable=True)
    what_not_building = Column(Text, nullable=True)
    build_summary = Column(Text, nullable=True)
    customer_location = Column(String(30), nullable=True)
    build_type = Column(String(30), nullable=True)
    platform = Column(String(30), nullable=True)
    core_product_types = Column(JSON, nullable=True)
    web_presences = Column(JSON, nullable=True)
    growth_and_sales = Column(JSON, nullable=True)
    community_and_engagements = Column(JSON, nullable=True)
    learning_and_onboardings = Column(JSON, nullable=True)
    payments = Column(JSON, nullable=True)
    escrow_support = Column(Boolean, nullable=True)
    messaging_apis = Column(JSON, nullable=True)
    ai_model_apis = Column(JSON, nullable=True)
    social_logins = Column(JSON, nullable=True)
    other_social_logins = Column(JSON, nullable=True)
    file_stores = Column(JSON, nullable=True)
    other_file_stores = Column(String(100), nullable=True)
    marketing_tools = Column(String(100), nullable=True)
    other_third_party_apis = Column(String(100), nullable=True)
    post_production_support = Column(Integer, nullable=True)


class ProjectStagingBaseDto(Object):
    fullname: str = Field(..., title="Full name", description="Your full name")
    email: str = Field(..., title="Email address", description="Your email address")
    phone: str = Field(..., title="Phone number", description="Your phone number")
    company_name: str = Field(..., title="Your Company/ Startup name", description="Your full name")

    budget: Optional[str] = None
    timeline: Optional[str] = None

    what_building: Optional[str] = None
    what_not_building: Optional[str] = None
    build_summary: Optional[str] = None
    customer_location: Optional[str] = None

    build_type: Optional[str] = None
    platform: Optional[str] = None
    core_product_types: Optional[List[str]] = None
    web_presences: Optional[List[str]] = None
    growth_and_sales: Optional[List[str]] = None
    community_and_engagements: Optional[List[str]] = None
    learning_and_onboardings: Optional[List[str]] = None

    payments: Optional[List[str]] = None
    escrow_support: Optional[bool] = None
    messaging_apis: Optional[List[str]] = None
    ai_model_apis: Optional[List[str]] = None
    social_logins: Optional[List[str]] = None
    other_social_logins: Optional[str] = None
    file_stores: Optional[List[str]] = None
    other_file_stores: Optional[str] = None
    marketing_tools: Optional[str] = None
    other_third_party_apis: Optional[str] = None
    post_production_support: Optional[int] = None # -1=not-sure, 0=no, 1=yes


class UpsertProjectStagingDto(ProjectStagingBaseDto):
    pass


class UpdateProjectStagingDto(ProjectStagingBaseDto):
    pass


class SearchProjectStagingDto(PageRequest, BaseQueryDto, UpsertProjectStagingDto):
    pass


class QueryProjectStagingDto(BaseQueryDto, UpsertProjectStagingDto):
    pass
