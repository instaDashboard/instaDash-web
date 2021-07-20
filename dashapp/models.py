from django.db import models

class Influencer(models.Model):
    unique_id = models.CharField(max_length=30, unique=True)
    insta_id = models.CharField(max_length=30, unique=True)
    username = models.CharField(max_length=30, blank=True, unique=True, null=True)
    follower = models.PositiveIntegerField()

    class Meta:
        db_table = 'influencer'


class Post(models.Model):
    unique_id = models.CharField(max_length=30)
    post_id = models.CharField(max_length=30, unique=True, null=False)
    comments_count = models.PositiveIntegerField()
    likes_count = models.PositiveIntegerField()
    post_date = models.DateField()
    
    class Meta:
        db_table = 'post'