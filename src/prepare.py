import pandas as pd
import sys
import logging

from dvc import api
from io import StringIO

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", 
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

logging.info("Fetching data from DVC")

# Fetch data from DVC
movie_data_path = api.read('dataset/movies.csv', remote='dataset-track', encoding="utf8") # el encoding es para que no de error al leer el csv
finantial_data_path = api.read('dataset/finantials.csv', remote='dataset-track', encoding="utf8")
opening_gross_path = api.read('dataset/opening_gross.csv', remote='dataset-track', encoding="utf8")

# Read data
movies_data = pd.read_csv(StringIO(movie_data_path))
finantials_data = pd.read_csv(StringIO(finantial_data_path))
opening_gross_data = pd.read_csv(StringIO(opening_gross_path))

#breakpoint() # it will stop the execution here and you can explore the data

# numeric columns
numeric_columns_mask = (movies_data.dtypes == float) | (movies_data.dtypes == int) | (movies_data.dtypes == 'int64')
numeric_columns = [column for column in numeric_columns_mask.index if numeric_columns_mask[column]]

# filter columns
movies_data = movies_data[numeric_columns + ['movie_title']]
finantials_data = finantials_data[['movie_title', 'production_budget', 'worldwide_gross']]

# merge data
fin_movie_data = pd.merge(finantials_data, movies_data, on='movie_title', how='left')
full_movie_data = pd.merge(opening_gross_data, fin_movie_data, on='movie_title', how='left')
full_movie_data = full_movie_data.drop(['gross', 'movie_title'], axis=1)

# save data
full_movie_data.to_csv('dataset/full_data.csv', index=False)

logger.info("Data fetched and prepared successfully")