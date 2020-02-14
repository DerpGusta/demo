from django.db import models


class Patient(models.Model):
    patient_ID=models.CharField(max_length=10,primary_key=True,null=False,default=0)
    Rating=models.CharField(max_length=10,null=True,default=None,blank=True)
    department=models.CharField(max_length=50,null=True,default=None,blank=False)
    area_of_issue=models.CharField(max_length=50,null=True,blank=True,default=None)
    explanation=models.CharField(max_length=200,null=True,blank=True,default=None)

    def __str__(self):
        return self.patient_ID

class HOD(models.Model):
    email=models.CharField(max_length=100,primary_key=True,default=None)
    password=models.CharField(max_length=20,default=None,blank=False)

    def __str__(self):
        return self.email

