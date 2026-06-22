from app.services.landing_service.stat_service import StatService
from app.services.landing_service.service_service import ServiceService
from app.services.landing_service.faq_service import FaqService


class LandingService:

    @staticmethod
    def get_landing_data():
        landing_data = {"stats":StatService.get_all_stats(),
                        "services":ServiceService.get_all_services(),
                        "faqs":FaqService.get_all_faqs()}
        return landing_data