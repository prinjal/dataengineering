#!/usr/bin/env python
# coding: utf-8

# ## Import pandas and read csv


import pandas as pd, argparse
from sqlalchemy import create_engine
from time import time
import os


def main(params):

    user=params.user
    password=params.password
    host=params.host
    port=params.port
    database=params.database
    table_name=params.table_name
    downloaded_file_name="output.csv.gz"
    csv_name="output.csv"
    url=params.url

    os.system("wget {0} -O {1}".format(url,downloaded_file_name))
    os.system("gunzip {0}".format(downloaded_file_name))


    df=pd.read_csv(csv_name,nrows=100)

    engine=create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")
    engine.connect()


    df_iter=pd.read_csv(csv_name,iterator=True,chunksize=100000)


    # Create a table in postgresql
    df.head(0).to_sql(name=table_name,con=engine,if_exists="replace")

    while True:
        try:
            ts_start=time()
            df=next(df_iter)
            df["tpep_pickup_datetime"]=pd.to_datetime(df["tpep_pickup_datetime"])
            df["tpep_dropoff_datetime"]=pd.to_datetime(df["tpep_dropoff_datetime"])
            df.to_sql(name=table_name,con=engine,if_exists="append")
            ts_end=time()

            print("inserted new chunk.... took %.3f time" % (ts_end-ts_start))
        except StopIteration:
            print("completed insertion process")
            break

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='What the program does')
    parser.add_argument("--user",help="Username of the postgres connection")
    parser.add_argument("--password",help="Username of the postgres connection")
    parser.add_argument("--host",help="Username of the postgres connection")
    parser.add_argument("--port",help="Username of the postgres connection")
    parser.add_argument("--database",help="Username of the postgres connection")
    parser.add_argument("--table_name",help="Username of the postgres connection")
    parser.add_argument("--csv_name",help="Username of the postgres connection")
    parser.add_argument("--url",help="Username of the postgres connection")
    args=parser.parse_args()
    main(args)


