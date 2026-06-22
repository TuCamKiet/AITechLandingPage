from pydantic import BaseModel
from typing import List, Optional
import stat_schema, feature_schema, service_schema,showcase_schema,preview_schema,pricing_schema, teammenber_schema, integration_schema,fap_schema,workflowstep_schema

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