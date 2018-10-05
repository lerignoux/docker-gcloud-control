# docker-gcloud-control
A docker container to start and stop google cloud instances

## tldr
Fill the credentials template using the service accoutn credentials downloaded from google cloud console as credentials.json
```
docker build -t docker-gcloud-control .
docker run -it -v credentials.json:/var/credentials.json -e gc_project=<instance_project_id> -e gc_zone=<instance_zone> -e gc_instance=<instance_name> docker-gcloud-control
```
