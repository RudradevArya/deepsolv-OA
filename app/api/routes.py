from fastapi import APIRouter, HTTPException
from app.services.scraper import scrape_linkedin_page
from app.services.database import get_page_from_db, save_page_to_db

router = APIRouter()

@router.get("/page/{page_id}")
async def get_page(page_id: str):
    #tryin to get page from db
    page = await get_page_from_db(page_id)
    
    if not page:
        #if no in db then go scrape
        try:
            page_data = await scrape_linkedin_page(page_id)
            page = await save_page_to_db(page_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    return page