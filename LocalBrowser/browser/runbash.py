import subprocess
from django.conf import settings
import os

class ManageGiveData():
    group_set = set(['genes', 'GWAS', 'LD', 'linkage', 'phastCons100Way', 'RADAR'])
    file_type_map = {'txt':'geneAnnot','bed':'bed','bw':'bigwig','interaction':'interaction'}
    
    def add(self, file_type, track_name, group_name, short_label, file_name):
        file_type = self.file_type_map.get(file_type)
        bash_path = os.path.join(settings.BASH_DIR, 'add_'+file_type+'.sh')
        subprocess.call([bash_path, track_name, group_name, short_label, file_name])


    def delete(self, group_name, track_name):
        if group_name in self.group_set:
            subprocess.call(['static/delete_file.sh', group_name, track_name])
        else:
            print("No such group!")


    def delete_all(self):
        bash_path = os.path.join(settings.BASH_DIR, 'delete_all.sh')
        subprocess.call([bash_path])

