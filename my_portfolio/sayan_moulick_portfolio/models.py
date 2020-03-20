from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'project'

# class Category(models.Model):
#     name = models.CharField(max_length=20)

#     class Meta:
#         db_table = 'category'

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     last_modified = models.DateTimeField(auto_now=True)
#     categories = models.ManyToManyField('Category', related_name='posts')

#     class Meta:
#         db_table = 'post'

# class Comment(models.Model):
#     author = models.CharField(max_length=60)
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     post = models.ForeignKey('Post', on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'comment'
