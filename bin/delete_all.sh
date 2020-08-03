#!/bin/bash
docker exec -it give /bin/bash -c "bash remove_data.sh -u root -p Admin2015 -r hg38 -a CONFIRM"
sleep 1s
docker exec -it give /bin/bash -c "bash initial_ref.sh -u root -p Admin2015 -r hg38 -s \"Homo sapiens\" -c human  -f /mnt/my_data/cytoBandIdeo.txt"
sleep 1s
docker exec -it give /bin/bash -c "bash add_trackGroup.sh  -u root -p Admin2015 -r hg38 -g \"txt\" -l \"Gene Annotation\" -o 1 -s 0"
sleep 1s
docker exec -it give /bin/bash -c "bash add_trackGroup.sh  -u root -p Admin2015 -r hg38 -g \"bed\" -l \"Bed\" -o 2 -s 0"
sleep 1s
docker exec -it give /bin/bash -c "bash add_trackGroup.sh  -u root -p Admin2015 -r hg38 -g \"bw\" -l \"BigWig\" -o 2 -s 0"
sleep 1s
docker exec -it give /bin/bash -c "bash add_trackGroup.sh  -u root -p Admin2015 -r hg38 -g \"interaction\" -l \"linkage interactions\" -o 3 -s 0"

