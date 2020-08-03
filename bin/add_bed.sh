#!/bin/bash
docker exec -it give /bin/bash -c "bash add_track_bed.sh -u root -p Admin2015 -r hg38 -t \"$1\" -g \"$2\" -l \"Null\" -s \"$3\" -o 1 -v full -f /mnt/my_data/$4"