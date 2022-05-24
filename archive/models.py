from django.db import models

# Create your models here.


class AbstractBlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField()
    source_name = models.TextField(max_length=100)
    date = models.DateField()
    archived = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.url


class Archive(AbstractBlogPost):
    pass
