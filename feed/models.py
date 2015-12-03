from __future__ import unicode_literals
from django.db import models
import newspaper

class Article(models.Model):
    url = models.TextField()
    title = models.TextField()
    text = models.TextField()

    @classmethod
    def ready(cls):
        return cls.objects.exclude(title='')

    @classmethod
    def pending(cls):
        return cls.objects.filter(title='')

    @classmethod
    def fetch_pending(cls):
        for a in cls.pending():
            a.fetch()

    def __str__(self):
        if self.title == '':
            return self.url
        else:
            return self.title

    def fetch(self):
        a = newspaper.Article(self.url, keep_article_html=True)
        a.download()
        a.parse()
        self.title = a.title
        self.text  = a.article_html
        self.save()
