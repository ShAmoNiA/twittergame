from django.db import models

class postClass(models.Model) :

    UserName = models.CharField(max_length=40,unique=False)
    message = models.CharField(max_length = 200)
    postId = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self) :
        return self.message

class replayClass(models.Model):
    mainPost = models.IntegerField()
    subPost = models.IntegerField()

    def __str__(self):
        return self.mainPost

class likesClass(models.Model):
    PostId = models.IntegerField()
    UserName = models.CharField(max_length=40,unique=False)

    def __str__(self):
        return self.PostId

