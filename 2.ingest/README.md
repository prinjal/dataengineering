## Invoking PostGres SQL with Docker

* Below-mentioned is a template to make connection with server
```
docker run -it \
services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - postgres-db-volume:/var/lib/postgresql/data
    port:
      5432:5432
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "airflow"]
      interval: 5s
      retries: 5
    restart: always
```


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

2. Install pgcli using ```pip3 install pgcli``` to access the Postgres Database
3. Command to run invoke Postgres database using pgcli:
   1. pgcli -h localhost -p 5432 -u root -d ny_taxi
   2. Downlad Jupyter using ```pip3 install jupyter```
   3. Instantiate Jupyter notebook using ```python3 -m notebook```
   4. Download dataset using ```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz ```