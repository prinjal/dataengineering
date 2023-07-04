## Schedule Jobs and Dockerize the Infrastructure

1. Create a docker file as one created [here](./Dockerfile) and a [docker-requirements.txt](./docker-requirements.txt) and copy in the root of the directory to make it working
2. Create a DockerContainer block from [Prefect Orion](http://localhost:4200/blocks/catalog/docker-container/create)
3. Deploy the build from python as mentioned [here](./deploy_docker_container.py)
4. Run the deployment with quick run


### Schedule a Job
1. To schedule a job, add cron and value while creating a deploy or the same can be done by creating a new schedule from Orion.