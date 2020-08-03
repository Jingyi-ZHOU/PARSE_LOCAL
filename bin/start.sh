#!/bin/bash

pip install -r $PWD/requirements.txt

docker pull zhonglab/give
sleep 1s
docker run -d -it -p 40080:80 -p 40443:443 -v $PWD/my_data:/mnt/my_data --name give zhonglab/give
sleep 5s
docker exec -it give /bin/bash -c "bash initial_ref.sh -u root -p Admin2015 -r hg38 -s \"Homo sapiens\" -c human  -f /mnt/my_data/cytoBandIdeo.txt"
sleep 1s
docker exec -it give /bin/bash -c "bash add_trackGroup.sh  -u root -p Admin2015 -r hg38 -g \"txt\" -l \"Gene Annotation\" -o 1 -s 0"
sleep 1s
docker exec -it give /bin/bash -c "bash add_trackGroup.sh  -u root -p Admin2015 -r hg38 -g \"bed\" -l \"Bed\" -o 2 -s 0"
sleep 1s
docker exec -it give /bin/bash -c "bash add_trackGroup.sh  -u root -p Admin2015 -r hg38 -g \"bw\" -l \"BigWig\" -o 2 -s 0"
sleep 1s
docker exec -it give /bin/bash -c "bash add_trackGroup.sh  -u root -p Admin2015 -r hg38 -g \"interaction\" -l \"linkage interactions\" -o 3 -s 0"

python $PWD/LocalBrowser/manage.py makemigrations
python $PWD/LocalBrowser/manage.py migrate
python $PWD/LocalBrowser/manage.py runserver 0.0.0.0:8000