from __future__ import unicode_literals
from django.db import models
import newspaper

class Article(models.Model):
    url = models.TextField()
    title = models.TextField()
    text = models.TextField()

    def fetch(self):
        a = newspaper.Article(self.url, keep_article_html=True)
        a.download()
        a.parse()
        self.title = a.title
        self.text  = a.article_html
        self.save()
