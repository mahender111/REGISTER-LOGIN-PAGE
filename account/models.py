from django.db import models
from django.utils import timezone

# Create your models here.
class Signup(models.Model):
    title= models.CharField(max_length=200,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    username = models.CharField(max_length=200,primary_key=True,blank=True)
    phone = models.CharField(max_length=13,null=True,blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email=models.EmailField(null=True,blank=True)
    password=models.CharField(max_length=15,null=True,blank=True)
    publish =models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)
     


    def __str__(self):
        return self.name 

    class Meta:
        # orderby=(-publish)
        db_table = ''
        managed = True
        verbose_name = 'Signup'
        verbose_name_plural = ('Signup')