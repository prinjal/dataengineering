## Invoking PostGres SQL with Docker

* Below-mentioned is a template to make connection with server
```

```


```
docker run -it \                           
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v /Users/prinjaldave/Library/CloudStorage/OneDrive-NortheasternUniversity/Northeastern/Self\ Learn/DataTalks\ Club/dataengineering/ingest/ny_taxi_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
```