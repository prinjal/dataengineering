from pathlib import Path
import pandas as pd
from prefect import flow, task, get_run_logger
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials
from prefect.infrastructure.process import Process


@task(log_prints=True)
def extract_from_gcs(color: str, year: int, month: int) -> Path:
    """_summary_
    GET_DIRECTORY ASYNC
    Copies a folder from the configured GCS bucket to a local directory.
    Defaults to copying the entire contents of the block's 
    bucket_folder to the current working directory.
    Args:
        color (str): _description_
        year (int): _description_
        month (int): _description_

    Returns:
        Path: _description_
    """    
    logger=get_run_logger()
    gcs_path=f"data/{color}/{color}_tripdata_{year}-{month:02}.parquet"
    gcp_cloud_storage_bucket_block = GcsBucket.load("dtc-gcs-bucket")    
    path=gcp_cloud_storage_bucket_block.download_object_to_path(
        from_path=gcs_path,
        to_path=f"/opt/prefect/data/{color}/{color}_tripdata_{year}-{month:02}.parquet"
    )

    return Path(f"/opt/prefect/{gcs_path}")


@task
def transform(path: str):
    df=pd.read_parquet(path)

    print(f"pre:missing passenger count: {df['passenger_count'].isin([0]).sum()}")

    df=df[df['passenger_count']!=0]

    print(f"post:missing passenger count: {df['passenger_count'].isin([0]).sum()}")


    return df

@task
def write_to_bq(df:pd.DataFrame) -> None:
    """_summary_
    Writes data to BigQuery
    Args:
        df (pd.DataFrame): DataFrame that needs to be written
    """
    gcp_credentials_block = GcpCredentials.load("dtc-gcs-bucket-keys")

    df.to_gbq(
        destination_table="ny_taxi.yellow_taxi_trips",
        project_id="nifty-matrix-385602",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="append"
    )


@flow
def etl_gcs_to_bq(color: str, year: int, month: int):
    """_summary_
    Gets file from gcs and transfers it to bq
    Args:
        color (str): Color of the taxi code
        year (int): Year for which data needs to be fetched
        month (int): Monht for which data needs to be fetched
    """        

    path=extract_from_gcs(color,year,month)
    transformed_data=transform(path)
    write_to_bq(transformed_data)

@flow
def etl_parent_flow(months: list[int]=[1,2] ,year: int = 2021, color: str = "yellow"):
    
    for month in months:
        etl_gcs_to_bq(color,year,month)
    


if __name__ == '__main__':
    etl_parent_flow(months,year,color)


