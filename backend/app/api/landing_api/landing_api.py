from fastapi import APIRouter
from app.services.landing_service.landing_service import LandingService
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.db_dependency import get_db

router = APIRouter(
    prefix="/landing",
    tags=["Landing"]
)


@router.get("")
def get_landing_page(db: Session = Depends(get_db)):
    return LandingService.get_landing_data(db)