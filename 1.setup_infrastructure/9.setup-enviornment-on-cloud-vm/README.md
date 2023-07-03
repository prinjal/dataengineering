## Setting Up Environment on Cloud VM

1. Create a ssh key using the below command:
   ```shell
   ssh-keygen -t rsa -f ~/.ssh/{SSH_KEY_FILENAME} -C {USERNAME} -b 2048
   ```
2. Change directory to /Users/{USERNAME}/.ssh
   ```shell
   cd /Users/{USERNAME}/.ssh
   ```
3. Copy public key using the below command:
   ```shell
   cat /Users/{USERNAME}/.ssh/SSH_KEY_FILENAME.pub
   ```
4. Navigate to compute engine in GCP and in metadata, add the copied public key under SSH keys

<details><summary>Create an instance</summary>

1. Under VM Instances, create a new VM Instance
2. Choose the region close to your location
3. e2-standard-4 is preferable machine type
4. Change bootdisk to Ubuntu (Ubuntu 20.04 LTS)
5. Change size to 30gb

</details>

<details><summary> SSH into VM Instance and configure it</summary>

1. Copy the External IP from the VM instance
2. SSH into instance (-i means identity)
   ```shell
   ssh -i ~/.ssh/gcp {USERNAME}@{EXTERNAL_IP}
   ```
3. To check the configuration fo the machine:
   ```shell
   htop
   ```
4. Use the below code sequentially to download anaconda in cloud machine
   ```shell
   wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh
   ```
   ```shell
   bash Anaconda3-2023.03-1-Linux-x86_64.sh
   ```
5. Create a config file for SSH
   ```
   cd {LOCATION_TO_SSH_FOLDER/LOCATION_TO HOME/.ssh/config}
   ```
   ```shell
   touch config
   ```
   ```shell
   code config
   ```
6. Below configuration needs to be added to the file
   ```config
   Host dtc-de-yellow-taxi-trips
         HostName {EXTERNAL_IP}
         User {USERNAME}
         IdentityFile {ABSOULTE_PATH_TO_SSH_KEY}
   ```
   ```
   source .bashrc
   ```
   * After this we can ssh directly using the below comand
   ```
   ssh {HostName}
   ```

7. Install docker in cloud VM
   ```shell
   sudo apt-get update
   ```
   ```shell
   sudo apt-get install docker.io
   ```

8. Install Remote - SSH extension and connect to Host using the bottom left icon <>

9. Follow the instructions from [this](https://github.com/sindresorhus/guides/blob/main/docker-without-sudo.md) link to use docker without sudo

10. Install docker compose from [this](https://github.com/docker/compose/releases) link
    1.  Download the latest version by copying the link of linu-x86
    2.  Create a new folder bin in the cloud vm
         ```shell
         mkdir bin
         ```
         ```shell
         cd bin
         ```
    3. Use the below comand to install docker compose
       ```
       wget https://github.com/docker/compose/releases/download/v2.19.0/docker-compose-darwin-x86_64 -O docker-compose
       ```
    4. Make this file executable
       ```shell
       chmod +x docker-compose
       ```
    5. Make the bin directory executable by opening .bashrc with nano/vim and    add the below path at the end
       ```
       export PATH="${HOME}/bin:${PATH}"
       ```
    6. Clone this github repository to the cloud vm
       ```shell
       git clone https://github.com/prinjal/dataengineering.git 
       ```
    7. Change Directory to 5_6.running-postgres-pgadmin-with-docker-compose_sql-refresher
    8. Instantiate docker-compose up
    9. Try connecting with database using below command:
         ```shell
         pgcli -h localhost  -u root -d ny_taxi
         ```

 11. Install pgcli using conda:
      ```shell
      conda install -c conda-forge pgcli
      ```  
      ```shell
      pip install -U mycli
      ```

</details>

<details><summary>Forward a port using VScode</summary>

* From the remote server right besides TERMINAL, click on the PORTS tab.
* Add a port forwarding rule using +
* Add 8080 (or any port that need to be forwarded) and press enter

</details>


<details><summary>Run the ingestion script on cloud vm</summary>

1. Download the data with below command:
   ```shell
   wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz
   ```

2. Use below to extract the file:
   ```shell
   gzip -d "filename"
   ```

3. Run the [upload_data.ipynb](./2.ingest/upload_data.ipynb) Jupyter notebook

4. Install Terraform from [here](https://developer.hashicorp.com/terraform/downloads) for linux AMD64
</details>


<details><summary>Configure gcloud cli on cloud VM</summary>

1. Change directory to gcp-service-account-auth-key under res
2. sftp to remote using:
   ```shell
   sftp {HOSTNAME}
   ```
3. Make .gc directory and change pwd to that directory
4. Use the below command to copy the non-auth gcp key:
   ```shell
   put {NAME_OF_GCP_KEY.json}
   ```
5. Export google application credentials using below command:
   ```shell
   export GOOGLE_APPLICATION_CREDENTIALS={ABSOLUTE_PATH.json}
   ```
6. Authenticate gcloud using below command:
   ```shell
   gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
   ```
7. Move to terraform directory and run init, plan, and apply to replicate the state file as in local machine
   1. The above will get the state of the cloud resources and create terraform.tfstate, and terraform.lock files to maintain integrity between local and cloud machine
8. Stop the vm:
   ```shell
   sudo shutdown
   ```

</details>