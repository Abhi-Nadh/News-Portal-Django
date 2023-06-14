from django.db import models
from django.contrib.auth.models import User


# from django.contrib.auth import get_current_user
class newsData(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=1000)
    image=models.FileField(upload_to='images')
    video=models.FileField(upload_to='videos')
    user_id = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

    
        
        
    # user_id = models.ForeignKey(User,null=True,on_delete=models.CASCADE) 


   
    

