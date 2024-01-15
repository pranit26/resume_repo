# backend/models.py
from django.db import models
from frontend.models import Candidates

class Resume(models.Model):
    resume_id = models.AutoField(primary_key=True)
    candidate = models.OneToOneField(Candidates, on_delete=models.CASCADE, unique=True, null=True)
    resume_file = models.FileField(upload_to='resumes/')


    class Meta:
        managed = False
        db_table = "resume"

    def __str__(self):
        return f"Resume(resume_id={self.resume_id},candidate='{self.candidate}',resume_file='{self.resume_file}')"
