from prefect.deployments import Deployment
from prefect.infrastructure.container import DockerContainer
from docker_etl_gcs_to_bq import etl_parent_flow

docker_block = DockerContainer.load("etl-docker-infra")

docker_dep = Deployment.build_from_flow(
    flow=etl_parent_flow,
    name='docker-flow',
    infrastructure=docker_block,
    parameters={
        "months":[1],
        "year":2021,
        "color":"yellow"
    }

)


if __name__ == '__main__':
    docker_dep.apply()