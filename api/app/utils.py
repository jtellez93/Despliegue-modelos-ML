import os

from joblib import load
from sklearn.pipeline import Pipeline
from pydantic import BaseModel
from pandas import DataFrame
from io import BytesIO

# function to get the model
def get_model() -> Pipeline:
    model_path = os.environ.get("MODEL_PATH", "model/model.pkl")
    with open(model_path, "rb") as model_file:
        model = load(BytesIO(model_file.read()))
    return model

# function to transform the request into a dataframe
def transform_to_dataframe(class_model: BaseModel) -> DataFrame:
    transition_dictionary = {key: [value] for key, value in class_model.model_dump().items()}
    data_frame = DataFrame(transition_dictionary)
    return data_frame