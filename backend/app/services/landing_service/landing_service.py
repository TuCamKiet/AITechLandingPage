from app.services.landing_service.stat_service import StatService
from app.services.landing_service.service_service import ServiceService
from app.services.landing_service.faq_service import FaqService
from app.services.landing_service.feature_service import FeatureService
from app.services.landing_service.pricing_service import PricingService
from app.services.landing_service.integration_service import IntegrationService
from app.services.landing_service.preview_service import PreviewService
from app.services.landing_service.showcase_service import ShowcaseService
from app.services.landing_service.teammember_service import TeamMemberService
from app.services.landing_service.workflowstep_service import WorkflowStepService

class LandingService:

    @staticmethod
    def get_landing_data():
        landing_data = {"stats":StatService.get_all_stats(),
                        "services":ServiceService.get_all_services(),
                        "faqs":FaqService.get_all_faqs(),
                        "features":FeatureService.get_all_features(),
                        "pricing":PricingService.get_all_pricing(),
                        "integrations":IntegrationService.get_all_integrations(),
                        "previews":PreviewService.get_all_previews(),
                        "showcases":ShowcaseService.get_all_showcases(),
                        "team":TeamMemberService.get_all_teammembers(),
                        "workflowSteps":WorkflowStepService.get_all_workflowsteps()}
                        
        return landing_data