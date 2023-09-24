import pandas as pd
import seaborn as sns

from matplotlib import pyplot as plt
from sklearn.pipeline import Pipeline
from joblib import dump

# function to recive model and save it
def update_model(model: Pipeline) -> None:
    dump(model, 'model/model.pkl')

# function to save simple metrics report
def save_simple_metrics_report(train_score: float, test_score: float, validation_score: float, model: Pipeline) -> None:
    with open('report.txt', 'w') as report_file:
        report_file.write('# Model Pipeline Description \n')

        for key, value in model.named_steps.items():
            report_file.write(f'### {key}: {value.__repr__()}\n' + '\n')

        report_file.write(f"### Train score: {train_score}\n")
        report_file.write(f"### Test score: {test_score}\n")
        report_file.write(f"### Validation score: {validation_score}\n")

# 
def get_model_performance_test_set(y_real: pd.Series, y_pred: pd.Series) -> None:
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.set_figheight(8)
    fig.set_figwidth(8)
    sns.regplot(x=y_pred, y=y_real, ax = ax)
    ax.set_title('Model Performance on Test Set')
    ax.set_xlabel('Predicted worldwide gross')
    ax.set_ylabel('Real worldwide gross')
    fig.savefig('performance.png')    