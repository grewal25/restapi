from django.db import models

class Post(models.Model):
    post_text=models.CharField(max_length=200)

    def __str__(self):
        return self.post_text

class Choice(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    likes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
