## Parameterization and Deployment

1. Copy the [etl_gc_to_bq](../3.gcp_gcs_to_bq/etl_gcs_to_bq.py) file.
2. Create color, month, and year parameters in etl_gcs_to_bq method.
3. Create a parent flow that runs on a for loop to execute the etlc_gcs_to_bq flow

### Build the deployment
1. Use the [concepts](https://docs.prefect.io/2.10.18/concepts/deployments/#deployment-definition) link to check the deployment architecture and cli code
2. To build a deploymnet:
   ```shell
    prefect deployment build {PATH_OF_FILE:PARENT_FLOW} -n {NAME_OF_FLOW}
   ```
3. Modify the yaml file to add parameters and workin_dir in the infrastructure as per the file linked [here](./etl_parent_flow-deployment.yaml)
4. Apply the deployment:
   ```shell
   prefect deployment apply {PATH_TO_YAML}
   ```

5. A [work pool](https://docs.prefect.io/2.10.18/concepts/work-pools/) task will be generated and we will need to create a agent to pick this work pool task
6. To create an [agent](https://docs.prefect.io/2.10.18/concepts/work-pools/#starting-an-agent):
   ```shell
   prefect agent start -p {WORK_POOL_NAME}
   ```
7. From the [UI](http://localhost:4200/deployments) start a quick job from the deployments