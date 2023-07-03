## Dockerizing the ingestion script

<details>
  <summary>Convert Jupyter Notebook to a python script</summary>
  
  1. Jupyter can convert the notebook to a [script](upload_data.py) using the below command:
      ```shell
      jupyter nbconvert --to=script {filename.ipynb}
      ```

  2. Install [argparse](https://docs.python.org/3/library/argparse.html) library to parse command line argument
  3. Refer [ingest_data.py](ingest_data.py) for parsing arguments and making the python script dynamic
</details>

<details>
  <summary>Run th script locally</summary>

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

</details>


<details>
<summary>Dockerize the script</summary>

1. Create a docker file with installing all the dependencies
  ```docker
  FROM python:3.9

  RUN apt-get install wget
  RUN pip install pandas sqlalchemy psycopg2

  WORKDIR /app

  COPY ingest_data.py ingest_data.py

  ENTRYPOINT [ "python", "ingest_data.py" ]
  ```

2. Create a docker image
    ```shell
    docker build -t taxi_ingest_data:v001 .
    ```

3. Run the docker image (make sure the [postgres server and pg-admin are running](../3.connect-pgadmin/README.md))
   * Note:host is selected as pg-database instead of localhost to connect to the postgresql
  
  ```shell
  URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

  docker run -it \
    --network=pg-network \
    taxi_ingest_data:v001 \
      --user=root\
      --password=root\
      --host=pg-database\
      --port=5432\
      --database=ny_taxi\
      --table_name=yellow_taxi_trips\
      --url=${URL}
  ```

</details>