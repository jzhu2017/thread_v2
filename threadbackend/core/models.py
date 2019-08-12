from django.db import models
from django.utils import timezone
from tinymce import HTMLField
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    tag = models.CharField(max_length=20)
    # content = models.TextField()
    content = HTMLField()
    date = models.DateField('date published')
    image = models.ImageField("Cover (best ratio is 3:2)", upload_to='static/imgs/articles')

    def get_relative_path(self):
        return "../" + str(self.image)

    def is_fashion(self):
        return self.tag == "fashion"

    def is_fashion(self):
        return self.tag == "art"

    def is_fashion(self):
        return self.tag == "lifestyle"

    def get_preview_text(self):
        return cleanhtml(self.content[:250])

    def get_article_link(self):
        return "?article_id=" + str(self.id)

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=20)

    def __str__(self):
        return self.title

class Issue(models.Model):
    term = models.CharField(max_length=100)
    title =  models.CharField(max_length=100)
    date = models.DateField('date published')
    issu = models.CharField(max_length=100)
    image = models.ImageField("Cover (best ratio is 3:2)", upload_to='static/imgs/issues')

    def get_relative_path(self):
        return "../" + str(self.image)

    def get_term_url(self):
        return "?issue_term=" + self.term

    def __str__(self):
        return self.term + ": " + self.title


class Email(models.Model):
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.email
