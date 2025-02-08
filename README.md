# US-visa-project-

Anaconda :https://www.anaconda.com/
Vs code: https:// code.visualstudio.com/download
git: https://git-scm.com/
flowchart : whimsical
mlops tools https:www.evidently.com/
MongoDB:https://account.mongodb.com/account/login

##### git command
git add .
git commit -m "updated"
git push origin main

#### how to run (creating enviroment)
;;; bash
conda create -n visa python =3.13.1 -y

conda activate visa

pip install -r requirements.txt



#### workflow

1.constants
2.entities
3.components
4.pipeline
5. Main file


##  Export the enviroment varibles using git bash(it sets the mongodb url as enviromental variable)

'''

# export MONGODB_URL="mongodb+srv://<username>:<password>...."

# export MONGO_URL=" mongodb+srv://mohan:krishna@cluster0.boljs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


# export AWS_ACCESS_KEY_ID = <AWS_ACCESS_KEY_ID>
# export AWS_SECRET_ACCESS_KEY =<AWS_SECERT_KEY_ID>






# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - <link>
	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_DEFAULT_REGION
   - ECR_REPO
   -MONGODB_URL
    










'''
