from django.db import models


class Tour(models.Model):
    image = models.ImageField(upload_to='galeria', null=False, blank=False)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)  
    content = models.TextField()

    def __str__(self):
        return self.title


class FeedBack(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
