from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    url = models.TextField()
    title = models.TextField()
    text = models.TextField()
