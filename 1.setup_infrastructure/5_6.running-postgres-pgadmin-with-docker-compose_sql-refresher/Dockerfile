FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app

COPY zone_ingest_data.py zone_ingest_data.py

ENTRYPOINT [ "python", "zone_ingest_data.py" ]