from django.db import models

# Create your models here.
class Track(models.Model):
    # file_type = models.TextChoices('geneAnnot','bed','bigwig')
    # track_id = models.AutoField(primary_key=True)
    # file_type = models.CharField(max_length=50)
    track_name = models.CharField(max_length=50, primary_key=True)
    # group = models.TextChoices('genes','GWAS','LD','RADAR','phastCons100way')
    # group = models.CharField(max_length=50)
    # label = models.CharField(max_length=100)
    # file_name = models.CharField(max_length=100)

    def __str__(self):
        return self.track_name