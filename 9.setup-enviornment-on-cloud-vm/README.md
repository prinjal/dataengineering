## Setting Up Environment on Cloud VM

1. Create a ssh key using the below command:
   ```ssh
   ssh-keygen -t rsa -f ~/.ssh/{SSH_KEY_FILENAME} -C {USER_NAME} -b 2048
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

