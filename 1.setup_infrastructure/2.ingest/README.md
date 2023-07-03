## Invoking PostGres SQL with Docker


1. Run docker container to connect with Postgres
```
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v /Users/prinjaldave/Library/CloudStorage/OneDrive-NortheasternUniversity/Northeastern/Self\ Learn/DataTalks\ Club/dataengineering/ingest/ny_taxi_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
```

1. Install [pgcli](https://pypi.org/project/pgcli/) using ```pip3 install pgcli``` to access the Postgres Database
2. Command to run invoke Postgres database using pgcli:
   1. pgcli -h localhost -p 5432 -u root -d ny_taxi
   2. Downlad Jupyter using ```pip3 install jupyter```
   3. Install Jupyter using -H (HOME) option ```sudo -H pip install jupyter```
   4. Instantiate Jupyter notebook using ```python3 -m notebook```
   5. Download dataset using ```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz ```
   6. pip3 install [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
   7. pip3 install [sqlalchemy](https://pypi.org/project/SQLAlchemy/)
3. The next step is to load data from jupyter notebook using pandas to Postgresql which has been done in the [upload_data.ipynb](2.ingest/upload_data.ipynb)