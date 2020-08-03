#!/bin/bash
docker exec -it give /bin/bash -c "bash add_track_interaction.sh -u root -p Admin2015 -r hg38 -t \"$1\" -g \"$2\" -l \"Null\" -s \"$3\" -o 1 -v full -q "0.37,1.32,1.78,2.19,2.60,2.97,3.43,3.85,4.34,4.90,5.48,6.16,6.94,8.01,9.05,10.41,12.37,14.88,19.84,31.77,290.17" -f /mnt/my_data/$4"
