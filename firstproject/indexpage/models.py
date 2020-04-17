from django.db import models

class Article(models.Model):

    ARTICLE_TYPE = (
        (1,'Type 1'),
        (2,'Type 2'),
    )

    title = models.CharField(max_length=50)
    body = models.TextField()
    # likes = models.IntegerField()
    type = models.IntegerField(choices= ARTICLE_TYPE)
    bub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title},{self.bub_date}'