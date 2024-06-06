from django.conf import settings
from django.db import models
from django.utils import timezone

'''
-defines our model (it is an object) by using 'class'
-post is the name of the model (always uppercase)
-models.Model means that the Post is a Django model
'''
class Post(models.Model):
    #defining the properties
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #models.CharField defines text with a limited number of characters
    title = models.CharField(max_length=200)
    #models.TextField defines text without a limit
    text = models.TextField()
    #defines date & time
    created_date = models.DateTimeField(default=timezone.now)
    #links to another model
    published_date = models.DateTimeField(blank=True, null=True)

    #defines a function/method called publish
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title