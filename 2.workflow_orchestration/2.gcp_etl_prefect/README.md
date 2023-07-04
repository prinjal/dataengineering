## Extract data, save locally and upload to GCS

* Check the [file](etl_web_to_gcs.py) for uploading script to GCS

<details><summary>Things to remember which is explicit from code</summary>

1. Register prefect_gcp block using below command:
   ```shell
   prefect block register -m prefect_gcp
   ```
2. Create a block from prefect console
   ```shell
   prefect orion start
   ```
3. From the blocks section, create a new GCS-bucket block
4. Add GCP credentials by creating a new IAM policy that has BigQuery admin and Storage Admin roles, add keys to it and copy the key in JSON format.
5. Paste it in the Service Key section
6. For more information check [here](https://github.com/padilha/de-zoomcamp/tree/master/week2)

</details>