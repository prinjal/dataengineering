## Setting Up Environment on Cloud VM

1. Create a ssh key using the below command:
   ```ssh
   ssh-keygen -t rsa -f ~/.ssh/{SSH_KEY_FILENAME} -C {USERNAME} -b 2048
   ```
2. Change directory to /Users/{USERNAME}/.ssh
   ```ssh
   cd /Users/{USERNAME}/.ssh
   ```
3. Copy public key using the below command:
   ```ssh
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

<details><summary> SSH into VM Instance</summary>

1. Copy the External IP from the VM instance
2. SSH into instance (-i means identity)
   ```ssh
   ssh -i ~/.ssh/gcp {USERNAME}@{EXTERNAL_IP}
   ```
3. To check the configuration fo the machine:
   ```ssh
   htop
   ```
4. Use the below code sequentially to download anaconda in cloud machine
   ```ssh
   wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh
   ```
   ```ssh
   bash Anaconda3-2023.03-1-Linux-x86_64.sh
   ```
5. Create a config file for SSH
   ```
   cd {LOCATION_TO_SSH_FOLDER}
   ```
   ```ssh
   touch config
   ```
   ```ssh
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
   ```ssh
   sudo apt-get update
   ```
   ```ssh
   sudo apt-get install docker.io
   ```

8. Install Remote - SSH extension and connect to Host using the bottom left icon <>

9. Follow the instructions from [this](https://github.com/sindresorhus/guides/blob/main/docker-without-sudo.md) link to use docker without sudo

10. Install docker compose from [this](https://github.com/docker/compose/releases) link
    1.  Download the latest version by copying the link of linu-x86
    2.  Create a new folder bin in the cloud vm
         ```ssh
         mkdir bin
         ```
         ```ssh
         cd bin
         ```
    3. Use the below comand to install docker compose
       ```
       wget https://github.com/docker/compose/releases/download/v2.19.0/docker-compose-darwin-x86_64 -O docker-compose
       ```
    4. Make this file executable
       ```ssh
       chmod +x docker-compose
       ```
    5. Make the bin directory executable by opening .bashrc with nano/vim and    add the below path at the end
       ```
       export PATH="${HOME}/bin:${PATH}"
       ``` 
    12. Clone this github repository to the cloud vm
       ```ssh
       git clone 
       ```
</details>

