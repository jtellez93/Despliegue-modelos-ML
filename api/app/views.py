from .models import Prediction_Request
from .utils import get_model, transform_to_dataframe

model = get_model()

def get_prediction(request: Prediction_Request) -> float:
    data_to_predict = transform_to_dataframe(request)
    prediction = model.predict(data_to_predict)[0]
    return max(prediction, 0) # don't return negative numbers