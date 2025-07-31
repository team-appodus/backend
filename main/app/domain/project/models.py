from typing import List, Optional

from appodus_utils import BaseEntity, PageRequest, BaseQueryDto, Object
from pydantic import Field, EmailStr
from sqlalchemy import Column, String, JSON, Boolean, Text, Integer


class Project(BaseEntity):
    __tablename__ = 'projects'
    fullname = Column(String(100), nullable=False)
    email = Column(String(60), nullable=False)
    phone = Column(String(17), nullable=False)
    company_name = Column(String(100), nullable=False)
    budget = Column(String(100), nullable=False)
    timeline = Column(String(100), nullable=False)
    what_building = Column(Text, nullable=False)
    what_not_building = Column(Text, nullable=False)
    build_summary = Column(Text, nullable=True)
    customer_location = Column(String(30), nullable=False)
    build_type = Column(String(30), nullable=False)
    platform = Column(String(30), nullable=False)
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
    post_production_support = Column(Integer, nullable=False)


class ProjectBaseDto(Object):
    fullname: str = Field(..., title="Full name", description="Your full name")
    email: str = Field(..., title="Email address", description="Your email address")
    phone: str = Field(..., title="Phone number", description="Your phone number")
    company_name: str = Field(..., title="Your Company/ Startup name", description="Your full name")

    budget: str  = Field(..., title="Budget range", description="Your budget for this project")
    timeline: str  = Field(..., title="Timeline", description="How soon do you want this project delivered")

    what_building: str  = Field(..., title="What you're building", description="Be specific about your core idea, target users, and main value proposition")
    what_not_building: str  = Field(..., title="What you're not building", description="This helps us focus on what matters most for your MVP")
    build_summary: Optional[str] = None
    customer_location: str  = Field(..., title="Customer primary location", description="This helps us consider timezone, regulations and local preferences")

    build_type: str  = Field(..., title="Full name", description="Your full name")
    platform: str  = Field(..., title="Full name", description="Your full name")
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
    post_production_support: int = Field(..., title="Post production support", description="How do we support you after production deployment") # -1=not-sure, 0=no, 1=yes


class _CreateProjectDto(ProjectBaseDto):
    pass

class CreateProjectDto(_CreateProjectDto):
    staging_id: str


class UpdateProjectDto(ProjectBaseDto):
    pass


class SearchProjectDto(PageRequest, BaseQueryDto, CreateProjectDto):
    pass


class QueryProjectDto(BaseQueryDto, _CreateProjectDto):
    pass
