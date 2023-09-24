import logging
import sys
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingRegressor

from utils import update_model, save_simple_metrics_report, get_model_performance_test_set


logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", 
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

# Load data
logger.info("Loading data")
data = pd.read_csv('dataset/full_data.csv')

# load model
logger.info("Loading model")
model = Pipeline([
    ('imputer', SimpleImputer(strategy='median', missing_values=np.nan)),
    ('core_model', GradientBoostingRegressor())
])

# split data
logger.info("Splitting data")
X_train, X_test, y_train, y_test = train_test_split(
    data.drop(['worldwide_gross'], axis=1),
    data['worldwide_gross'],
    test_size=0.35,
    random_state=42
)

# setting Hyperparameters
logger.info("Setting hyperparameters to tune")
param_tunning = {
    'core_model__n_estimators': range(20, 301, 20)
}

grid_search = GridSearchCV(
    model,
    param_grid=param_tunning,
    cv=5,
    scoring='r2'
)

# tune model
logger.info("Starting model tuning")
grid_search.fit(X_train, y_train)

# cross validate model
logger.info("Cross validating with best model")
final_result = cross_validate(
    grid_search.best_estimator_,
    X_train,
    y_train,
    cv=5,
    return_train_score=True
)

train_score = np.mean(final_result['train_score'])
test_score = np.mean(final_result['test_score'])

assert train_score > 0.7, "Train score is too low"
assert test_score > 0.65, "Test score is too low"

logger.info(f"Train score: {train_score}")
logger.info(f"Test score: {test_score}")

# update model
logger.info("Updating model")
update_model(grid_search.best_estimator_)
logger.info("Model updated successfully")

# model report
logger.info("Generating model report")
validation_score = grid_search.best_estimator_.score(X_test, y_test)
save_simple_metrics_report(train_score, test_score, validation_score, grid_search.best_estimator_)

# graph report
y_test_pred = grid_search.best_estimator_.predict(X_test)
get_model_performance_test_set(y_test, y_test_pred)
logger.info("Model report generated successfully")

logger.info("Training process finished successfully")