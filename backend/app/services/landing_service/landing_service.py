from sqlalchemy.orm import Session

from app.services.landing_service.stat_service import get_all_stats
from app.services.landing_service.service_service import get_all_services
from app.services.landing_service.faq_service import get_all_faqs
from app.services.landing_service.feature_service import get_all_features
from app.services.landing_service.pricing_service import get_all_pricing
from app.services.landing_service.integration_service import get_all_integrations
from app.services.landing_service.preview_service import get_all_previews
from app.services.landing_service.showcase_service import get_all_showcases
from app.services.landing_service.teammember_service import get_all_team_members
from app.services.landing_service.workflowstep_service import get_all_workflow_steps

class LandingService:

    @staticmethod
    def get_landing_data(db: Session):
        landing_data = {"stats":get_all_stats(db),
                        "services":get_all_services(db),
                        "faqs":get_all_faqs(db),
                        "features":get_all_features(db),
                        "pricing":get_all_pricing(db),
                        "integrations":get_all_integrations(db),
                        "previews":get_all_previews(db),
                        "showcases":get_all_showcases(db),
                        "team":get_all_team_members(db),
                        "workflowSteps":get_all_workflow_steps(db)}
                        
        return landing_data