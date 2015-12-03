from __future__ import unicode_literals
from django.db import models
import newspaper

class Article(models.Model):
    url = models.TextField(null=True)
    title = models.TextField(null=True)
    text = models.TextField(null=True)

    @classmethod
    def ready(cls):
        return cls.objects.filter(title__isnull=False)

    @classmethod
    def pending(cls):
        return cls.objects.filter(title__isnull=True)

    @classmethod
    def fetch_pending(cls):
        for a in cls.pending():
            a.fetch()

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.url

    def fetch(self):
        a = newspaper.Article(self.url, keep_article_html=True)
        a.download()
        a.parse()
        self.title = a.title
        self.text  = a.article_html
        self.save()
