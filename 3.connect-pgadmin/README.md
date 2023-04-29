## What is pgAdmin?
* PGAdmin is a web-based Graphical User Interface (GUI) management application used to communicate with Postgres and derivative relational databases on both local and remote servers.
  
&nbsp;

<details> <summary>How to connect with pgAdmin?</summary>

```shell
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  dpage/pgadmin4
```
</details>

&nbsp;


### Running postgres and pgAdmin together

1.  Create a Network
```
docker network create pg-network
```
2. Run postgres by including network and name
```
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v /Users/prinjaldave/Library/CloudStorage/OneDrive-NortheasternUniversity/Northeastern/Self\ Learn/DataTalks\ Club/dataengineering/ingest/ny_taxi_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13
```
3. Run pgadmin with network and name
```
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pgadmin-2 \
  dpage/pgadmin4
```