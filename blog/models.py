from django.db import models

# Create your models here.

class Blog(models.Model):
    creator=models.ForeignKey('auth.User',related_name='blogs', on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['created']

    def __str__(self):
        return self.title

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=100, blank=False)
    blog=models.ForeignKey('Blog',related_name='comments',on_delete=models.CASCADE)
    creator=models.ForeignKey('auth.User',related_name='comments',on_delete=models.CASCADE)

    class Meta:
        ordering=['created']