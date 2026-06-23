from app.data.landing_data import faqs
from app.schemas.landing_schema.faq_schema import FAQ


class FaqService:
    @staticmethod
    def get_all_faqs() -> list[FAQ]:
        return [FAQ(**item) for item in faqs]