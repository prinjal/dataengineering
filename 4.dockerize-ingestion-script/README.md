## Dockerizing the ingestion script

### Convert the jupyter notebook to a python script
1. Jupyter can convert the notebook to a [script](upload_data.py) using the below command:
  * ```jupyter nbconvert --to=script {filename.ipynb}```
2. Install [argparse](https://docs.python.org/3/library/argparse.html) library to parse command line argument
3. Refer [ingest_data.py](ingest_data.py) for parsing arguments and making the python script dynamic
4. Run the script using the below-mentioned command:
    ```
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

    wget ${URL}