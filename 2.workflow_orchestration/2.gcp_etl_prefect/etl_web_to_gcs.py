from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket


@task(retries=3)
def fetch(dataset_url:str) -> pd.DataFrame:
    """_summary_

    Args:
        dataset_url (str): URL to fetch dataset

    Returns:
        pd.DataFrame: Dataframe gotten from the URL
    """    
    df=pd.read_csv(dataset_url)

    return df

@task()
def clean(df:pd.DataFrame) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): Returns cleaned dataframe

    Returns:
        pd.DataFrame: Gets uncleaned dataframe
    """    
    df["tpep_pickup_datetime"]=pd.to_datetime(df["tpep_pickup_datetime"])
    df["tpep_dropoff_datetime"]=pd.to_datetime(df["tpep_dropoff_datetime"])
    print(df.head(2))
    print(f"columns: {df.dtypes}")
    print(f"rows: {len(df)}")

    return df

@task()
def write_local(df:pd.DataFrame, color: str, dataset_file: str) -> Path:
    """_summary_
    Writing data locally
    Args:
        df (pd.DataFrame): gets the dataframe

    Returns:
        Path: returns the path where dataframe is saved locally
    """    

    Path(f"data/{color}").mkdir(parents=True, exist_ok=True)
    path = Path(f"data/{color}/{dataset_file}.parquet")
    df.to_parquet(path,compression="gzip")
    return path

@task()
def write_to_gcs(path:Path) -> None:
    """_summary_
    Writing data to gcs
    Args:
        path (Path): path from where data needs to be fetched
    """    

    gcp_cloud_storage_bucket_block = GcsBucket.load("dtc-gcs-bucket")
    gcp_cloud_storage_bucket_block.upload_from_path(
        from_path=f"{path}",
        to_path=path
    )
    return



@flow(name="ETL Web to GCS")
def etl_web_to_gcs() -> None:
    """_summary_
    This is the main function to drive the etl workflow
    """
    color="yellow"
    year=2021
    month=1
    dataset_file=f"{color}_tripdata_{year}-{month:02}"
    dataset_url=f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{dataset_file}.csv.gz"


    raw_df=fetch(dataset_url)
    cleaned_df=clean(raw_df)
    path=write_local(cleaned_df, color=color, dataset_file=dataset_file)
    write_to_gcs(path)



if __name__ == '__main__':
    etl_web_to_gcs()