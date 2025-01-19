from fastapi import FastAPI, HTTPException, Query
from api.utils import extract_reviews

app = FastAPI()

@app.get("/api/reviews")
async def get_reviews(page: str = Query(..., description="URL of the product page")):
    """
    API endpoint to extract reviews from the given product page.
    """
    try:
        reviews_data = await extract_reviews(page)
        return reviews_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting reviews: {str(e)}")
