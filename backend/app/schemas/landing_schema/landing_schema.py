from pydantic import BaseModel
from typing import List
from stat_schema import Stat
from feature_schema import Feature
from service_schema import Service
from showcase_schema import Showcase
from preview_schema import Preview
from pricing_schema import Pricing
from workflowstep_schema import WorkflowStep
from integration_schema import Integration
from backend.app.schemas.landing_schema.faq_schema import FAQ
from teammenber_schema import TeamMember

class LandingResponse(BaseModel):
    stats: List[Stat]
    features: List[Feature]
    services: List[Service]
    showcases: List[Showcase]
    workflowSteps: List[WorkflowStep]
    integrations: List[Integration]
    previews: List[Preview]
    pricing: List[Pricing]
    faqs: List[FAQ]
    team: List[TeamMember]

# class Stat(BaseModel):
#     label: str
#     value: str


# class Feature(BaseModel):
#     icon: str
#     title: str
#     description: str


# class Service(BaseModel):
#     icon: str
#     name: str
#     summary: str


# class Showcase(BaseModel):
#     icon: str
#     title: str
#     description: str
#     metric: str


# class WorkflowStep(BaseModel):
#     step: str
#     title: str
#     detail: str


# class Integration(BaseModel):
#     name: str
#     icon: str


# class Preview(BaseModel):
#     quote: str
#     author: str
#     role: str


# class Pricing(BaseModel):
#     tier: str
#     monthly: str
#     annual: str
#     description: str
#     features: List[str]
#     popular: Optional[bool] = False


# class FAQ(BaseModel):
#     q: str
#     a: str


# class TeamMember(BaseModel):
#     name: str
#     role: str