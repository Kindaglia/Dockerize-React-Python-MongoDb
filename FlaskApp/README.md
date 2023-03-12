# How to dockerize and host a flask app 

## Create application flask
see app [main script](app.py)

## Create Dockerfile and docker-compose 
If you want start project with this command
```
docker compose up
```

## Create istance EC2 on [AWS](https://aws.amazon.com/it/)
- Login on AWS
- Search EC2
- Click Start Istance
- Add Name app
- In Amazon Machine Image select Ubuntu
- Name key private: create your key and save key .pem
![Screenshot](img/istance.png)

## After creation
- Go to istance EC2
- Click on your id istance
- click security
- click grup security
- click operation -> mod rule input 
- Change Type from SSH to All Traffic
- Save rules  
Test net with  IPv4 pubblic of your istance:
```
ping <ip address> 
```

## Connect to Machine with ssh and VScode
- install [this](https://code.visualstudio.com/docs/remote/ssh-tutorial) extension for VScode
- in ssh config add this  
```
Host HostingName
  HostName IPv4 
  User ubuntu
  IdentityFile path_key.pem
```

## Start Docker
- open new terminal on VScode and install docker, [script](https://github.com/docker/docker-install) 

```
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

- Install git 
```
sudo apt install git
```

- Clone [this](https://github.com/Kindaglia/Dockerize-React-Python-MongoDb.git) repository
```
mkdir dockerApp

cd dockerApp

git clone https://github.com/Kindaglia/Dockerize-React-Python-MongoDb.git

cd Dockerize-React-Python-MongoDb/

cd FlaskApp

sudo docker compose up
```
