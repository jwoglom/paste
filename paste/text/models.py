from django.db import models

class Author(models.Model):
    name = models.CharField(default="Anonymous", max_length=1000)

    def __unicode__(self):
        return self.name
class Paste(models.Model):
    title = models.CharField(default="", max_length=1000)
    contents = models.TextField(default="")
    author = models.ForeignKey('Author', null=True)
    private = models.BooleanField(default=False)
    code = models.BooleanField(default=True)
    identifier = models.TextField(default="")

    def __unicode__(self):
        return self.title
