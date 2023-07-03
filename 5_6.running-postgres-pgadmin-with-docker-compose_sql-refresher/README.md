## Running Postgres and pgAdmin using docker compose

### What is Docker Compose?
* Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.


<details>
<summary>Template for creating a yaml file</summary>

```shell
    version: "3.9"
    services:
    web:
        build: .
        ports:
        - "8000:5000"
        volumes:
        - .:/code
        environment:
        FLASK_DEBUG: "true"
    redis:
        image: "redis:alpine"
```
</details>

* Create a [docker-compose yaml](docker-compose.yaml) file using the above template. 

<details>
<summary> Run multiple containers together </summary>

1. Intiating docker-compose
    ```
    docker-compose up
    ```
2. Ending docker compose
   ```
    docker-compose down
   ```    
3. Running docker-compose in detach mode
   ```
   docker-compose up -d
   ```

</details>

<details><summary>If pgadmin4 throws an error while initializing</summary>

1. Change directory to 2.ingest (the location where we are pointing volume)
2. Provide access to the data_pgadmin folder using the below command:
   ```
    sudo chown -R 5050:5050 ${DATA_PATH_HOST}/pgadmin
   ```
3. If the above doesn't work follow [this](https://stackoverflow.com/questions/64781245/permission-denied-var-lib-pgadmin-sessions-in-docker) link to debug this issue further

</details>

<details><summary>To run ingestion script after composing postgres db and pgadmin</summary>

```shell
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

docker run -it \
  --network={network_name (docker network ls)} \
  taxi_ingest_data:v001 \
    --user=root\
    --password=root\
    --host=pgdatabase\
    --port=5432\
    --database=ny_taxi\
    --table_name=yellow_taxi_trips\
    --url=${URL}
```

</details>