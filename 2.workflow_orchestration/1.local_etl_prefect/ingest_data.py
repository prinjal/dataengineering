#!/usr/bin/env python
# coding: utf-8

# ## Import pandas and read csv


import pandas as pd, argparse
from sqlalchemy import create_engine
from time import time
from datetime import timedelta
import os
from prefect import flow, task
from prefect.tasks import task_input_hash
from prefect_sqlalchemy import SqlAlchemyConnector

@task(log_prints=True,retries=3,cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def extract_data_task(url):
    downloaded_file_name="output.csv.gz"
    csv_name="output.csv"

    os.system("wget {0} -O {1}".format(url,downloaded_file_name))
    os.system("gunzip {0}".format(downloaded_file_name))


    df=pd.read_csv(csv_name,nrows=100)

    df_iter=pd.read_csv(csv_name,iterator=True,chunksize=100000)
    df=next(df_iter)

    df["tpep_pickup_datetime"]=pd.to_datetime(df["tpep_pickup_datetime"])
    df["tpep_dropoff_datetime"]=pd.to_datetime(df["tpep_dropoff_datetime"])

    return df

@task(log_prints=True)
def transform_data_task(df):
    print(f"pre:missing passenger count: {df['passenger_count'].isin([0]).sum()}")

    df=df[df['passenger_count']!=0]

    print(f"post:missing passenger count: {df['passenger_count'].isin([0]).sum()}")

    return df

@task(log_prints=True,retries=3)
def ingest_data_task(params,df):

    # user=params.user
    # password=params.password
    # host=params.host
    # port=params.port
    # database=params.database
    table_name=params.table_name
    

    
    database_block = SqlAlchemyConnector.load("sql-alchemy-connector")
    with database_block.get_connection(begin=False) as engine:
    # Create a table in postgresql
        df.head(0).to_sql(name=table_name,con=engine,if_exists="replace")
        df.to_sql(name=table_name,con=engine,if_exists="append")

    # while True:
    #     try:
    #         ts_start=time()
    #         df=next(df_iter)
    #         df["tpep_pickup_datetime"]=pd.to_datetime(df["tpep_pickup_datetime"])
    #         df["tpep_dropoff_datetime"]=pd.to_datetime(df["tpep_dropoff_datetime"])
    #         df.to_sql(name=table_name,con=engine,if_exists="append")
    #         ts_end=time()

    #         print("inserted new chunk.... took %.3f time" % (ts_end-ts_start))
    #     except StopIteration:
    #         print("completed insertion process")
    #         break

@flow(name="Sub Flow",log_prints=True)
def sub_flow(url: str):
    print(f"Logging data for {url}")


@flow(name="Ingest Flow")
def main_flow(args):

    sub_flow(args.url)
    raw_data=extract_data_task(args.url)
    data=transform_data_task(raw_data)
    ingest_data_task(args,data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='What the program does')
    # parser.add_argument("--user",help="Username of the postgres connection")
    # parser.add_argument("--password",help="Username of the postgres connection")
    # parser.add_argument("--host",help="Username of the postgres connection")
    # parser.add_argument("--port",help="Username of the postgres connection")
    # parser.add_argument("--database",help="Username of the postgres connection")
    parser.add_argument("--table_name",help="Username of the postgres connection")
    # parser.add_argument("--csv_name",help="Username of the postgres connection")
    parser.add_argument("--url",help="URL to be downloaded")
    args=parser.parse_args()
    main_flow(args)