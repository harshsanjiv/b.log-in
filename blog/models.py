from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=280)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return (self.title)
        
    def get_absolute_url(self):
        return reverse('blog-home')
class Comment(models.Model):
    content=models.CharField(max_length=140)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post_author=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    date_posted=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return (self.content)
    
    def get_absolute_url(self):
        return reverse('post-detail',args=[str(self.post_author.id)])
        
    class Meta:
        ordering=['-date_posted']