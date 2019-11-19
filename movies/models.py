from django.db import models

class Classification(models.Model):
    text = models.CharField(max_length=10, null=False)

    def __str__ (self):
        return self.text

class Genre(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__ (self):
        return self.name

class Provider(models.Model):
    name = models.CharField(max_length=50, null=False)
    url = models.URLField(blank=True)

    def __str__ (self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100, null=False)
    summary = models.CharField(max_length=5000, null=False)
    duration = models.DurationField(blank=True)
    release_date = models.DateField(blank=True)
    classification = models.ForeignKey(Classification, on_delete=models.DO_NOTHING)
    genre = models.ManyToManyField(Genre)
    provider = models.ManyToManyField(Provider)

    def __str__ (self):
        return self.title