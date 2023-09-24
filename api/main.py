from fastapi import FastAPI
from .app.models import Prediction_Request, Prediction_Response
from .app.views import get_prediction

# create service and endpoints
app = FastAPI(docs_url="/")

@app.post("/v1/prediction")
def make_model_prediction(request: Prediction_Request):
    return Prediction_Response(worldwide_gross=get_prediction(request))