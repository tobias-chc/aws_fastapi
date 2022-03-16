# aws_fastapi

## Step 1: Create the app and Dockerfile

Create the app and the Dockerfile, in my case this is my folder structure:

--------

    ├── app                    <- Folder with the apps files.
    │   └── main.py            <- Python script with the fastapi code.
    │
    ├── Dockerfile             
    │
    ├── requirements.txt       <- The requirements file for reproducing the app environment, e.g.
    │                             generated with `pip freeze > requirements.txt`

## Step 2: Build and test the Dockerfile locally


1. Build the Dockerfile:

```sh
docker build -t aws_fastapi_image .
```

2. Run a container of the image locally to check that everything works.

```sh
docker run -p 1234:8080 aws_fastapi_image
```

Go to: http://localhost:1234/ if all its ok then next step else review your code/Dockerfile, etc.

## Step 3: Push your image to your repositories on docker hub.

1. Register on [Docker Hub](https://hub.docker.com/)

2. Tag your image with the following command:

   ```sh
   docker tag <IMAGE_NAME> <DOCKER_ACCOUNT_NAME>/<CUSTOM_IMAGE_NAME>
   ```
 where 
 - `DOCKER_ACCOUNT_NAME` - is your account on Docker Hub
 - `CUSTOM_IMAGE_NAME` - the custom name of the image.

 In my case:

  ```sh
 docker tag aws_fastapi_image tobiaschc/aws_ec2
 ```
   
  
3. Log in to Docker Hub from your terminal:
   ```sh
   docker login
   ```
4. Push the docker image to Docker Hub:
   ```sh
   docker push <DOCKER_ACCOUNT_NAME>/<CUSTOM_IMAGE_NAME>
   ```
5. See if you can find the image in your [repositories](https://hub.docker.com/repositories) in the Docker Hub.


## Step 4: Create an EC2 instance

1. Launch an EC2 instances in AWS as we did in class.


## Step 5: Install Docker in the instance:

2. Install Docker in the instance:

 ```sh
  sudo apt update
 ```

 Downloading Dependencies

Allow your Ubuntu 20.04 system to access the Docker repositories over HTTPS by running:
 ```sh
  sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
 ```

 Adding Docker’s GPG Key.

Next, add the GPG key to ensure the authenticity of the software package:

  ```sh
 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
 ```
Installing the Docker Repository:
 ```sh
 sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs)  stable"
 ```

Installing the Latest Docker:

```sh
    sudo apt update
 ```

```sh
    sudo apt-get install docker-ce
 ```

Verify the installation:

```sh
    docker --version
 ```

 Enable Docker services:

 ```sh
 sudo systemctl start docker
 ```

 ## Step 5: Pull the docker Image

 ```sh
sudo docker pull tobiaschc/aws_ec2
 ```

 Verify your images:

 ```sh
sudo docker images
 ```


## Step 6: Run the app

 ```sh
sudo docker run -p 80:8080 tobiaschc/aws_ec2
 ```

## Step 7: Access the app from your computer or any device:

Go to your Public IP address

```sh
https://3.91.195.3/
```

the app should be running!





 