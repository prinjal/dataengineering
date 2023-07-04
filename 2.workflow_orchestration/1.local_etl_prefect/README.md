## Ingest Data locally with prefect

<details><summary>Run the Ingest Data Script</summary>

1. Copy the ingest_data.py from [here](../1.setup_infrastructure/4.dockerize-ingestion-script/ingest_data.py)

2. Install miniconda to access conda from [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

3. Create a new conda environment
   ```shell
   conda create -n dtc_yellow_taxi python=3.11
   ```
   ```shell
   conda deactivate
   ```
   ```shell
   conda activate dtc_yellow_taxi
   ```

4. Install dependencies from requirements.txt
   ```shell
   pip install -r requirements.txt
   ``` 

5. Open a new terminal and run dcoker-compose up for firing up postgres and pgadmin from "/1.setup_infrastructure/5_6.running-postgres-pgadmin-with-docker-compose_sql-refresher"

<details>
  <summary>Run the script locally</summary>

  * Run the script locally first using the below-mentioned command:
    ```shell
    URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

    python3 ingest_data.py\
        --user=root\
        --password=root\
        --host=localhost\
        --port=5432\
        --database=ny_taxi\
        --table_name=yellow_taxi_trips\
        --url=${URL}

    ```

1. Create flows and tasks to break down Extract, Transfer, and Load part of the whole script as mentioned in this [file](ingest_data.py)
2. Create a sql alchemy block after running prefect orion start to store the parameters to connect with sql alchemy
   1. Use [this](https://github.com/padilha/de-zoomcamp/tree/master/week2) link for more details

</details>

</details>