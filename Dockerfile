FROM prefecthq/prefect:2.7.7-python3.9

COPY docker-requirements.txt .

RUN pip install -r docker-requirements.txt --trusted-host pypi.python.org --no-cache-dir


COPY 2.workflow_orchestration/5.schedule_and_docker_infra /opt/prefect/flows
COPY 2.workflow_orchestration/2.gcp_etl_prefect/data /opt/prefect/data