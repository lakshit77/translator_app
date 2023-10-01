sudo docker login -u $REGISTRY_NAME -p $REGISTRY_PASS

if [ sudo docker ps -aq ]
then 
    sudo docker ps -aq | sudo xargs docker stop | sudo xargs docker rm 
fi

sudo docker run -d -p 8000:8000 $IMAGE_NAME