## Schedule Jobs and Dockerize the Infrastructure

1. Create a docker file as one created [here](./Dockerfile) and a [docker-requirements.txt](./docker-requirements.txt) and copy in the root of the directory to make it working
2. Create a DockerContainer block from [Prefect Orion](http://localhost:4200/blocks/catalog/docker-container/create)
3. Deploy the build from python as mentioned [here](./deploy_docker_container.py)
4. Change the api config path with from [this](https://docs.prefect.io/2.10.18/concepts/settings/#setting-and-clearing-values) link or below command:
   ```shell
   prefect config set PREFECT_API_URL="http://127.0.0.1:4200/api"
   ```
5. Run the deployment with quick run


### Schedule a Job
1. To schedule a job, add cron and value while creating a deploy or the same can be done by creating a new schedule from Orion.