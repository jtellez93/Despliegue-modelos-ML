from pydantic import BaseModel

class Prediction_Request(BaseModel):
    opening_gross: float
    screens: float
    production_budget: float
    title_year: int
    aspect_ratio: float
    duration: float
    cast_total_facebook_likes: float
    budget: float
    imdb_score: float

class Prediction_Response(BaseModel):
    worldwide_gross: float