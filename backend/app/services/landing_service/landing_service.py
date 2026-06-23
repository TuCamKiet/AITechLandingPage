from sqlalchemy.orm import Session

from app.services.landing_service.stat_service import get_all_stats
from app.services.landing_service.service_service import get_all_services
from app.services.landing_service.faq_service import FaqService
from app.services.landing_service.feature_service import get_all_features
from app.services.landing_service.pricing_service import PricingService
from app.services.landing_service.integration_service import IntegrationService
from app.services.landing_service.preview_service import PreviewService
from app.services.landing_service.showcase_service import get_all_showcases
from app.services.landing_service.teammember_service import TeamMemberService
from app.services.landing_service.workflowstep_service import get_all_workflow_steps

class LandingService:

    @staticmethod
    def get_landing_data(db: Session):
        landing_data = {"stats":get_all_stats(db),
                        "services":get_all_services(db),
                        "faqs":FaqService.get_all_faqs(),
                        "features":get_all_features(db),
                        "pricing":PricingService.get_all_pricing(),
                        "integrations":IntegrationService.get_all_integrations(),
                        "previews":PreviewService.get_all_previews(),
                        "showcases":get_all_showcases(db),
                        "team":TeamMemberService.get_all_teammembers(),
                        "workflowSteps":get_all_workflow_steps(db)}
                        
        return landing_data