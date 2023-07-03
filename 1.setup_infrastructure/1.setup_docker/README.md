## Writing a Docker File


- There are various commands to write a docker file


  1. FROM: Takes the base package to create the first layer of the docker file
  2. RUN: Runs the statement once the docker image has been instantiated
  3. WORKDIR: To change the working directory in the docker container
  4. COPY: Copies the file from source (local) to destination (docker container)
  5. ENTRYPOINT: Choose the entry point to execute the commands once docker container is invoked




## Building a Docker file
1. To build a docker image: 
    * -t: tag
    * {path}: directory from where the docker file needs to be build
    ```
    docker build -t {name_of_the_image}:{tag_for_image} {path}

    docker build -t test:test_tag .
    ```
2. To run a docker image:
   * -it: invoke in interactive command line
   * {parameters}: include all the sys.argv parameters
   ```
   docker run -it {name_of_the_image}:{tag_for_image} {parameters}

   docker run -it test:pandas 2022-12-10 hello
   ```
 