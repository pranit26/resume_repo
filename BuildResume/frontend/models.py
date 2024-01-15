from django.db import models

# Create your models here.


class Candidates(models.Model):
    candidate_id = models.AutoField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    contact_number = models.IntegerField()
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    tech_skills = models.CharField(max_length=250)
    experience=models.IntegerField()


    class Meta:
        managed = False
        db_table = 'candidates'

    def __str__(self):
        return f"Candidates(candidate_id={self.candidate_id},name='{self.name}',address='{self.address}',contact_number='{self.contact_number}',email='{self.email}',location='{self.location}',tech_skills='{self.tech_skills}',experience='{self.experience}')"
    