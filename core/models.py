from django.db import models


class Direction(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name='Direction Name')
    slug = models.SlugField(unique=True,
                            verbose_name='Direction Slug')
    sort_number = models.PositiveBigIntegerField(
        verbose_name='Direction Sort Number')


class Doctor(models.Model):
    name = models.CharField(verbose_name='Doctor Name', max_length=100)
    slug = models.SlugField(unique=True, verbose_name='Doctor Slug')
    direction = models.ManyToManyField(Direction, related_name='Direction')
    description = models.TextField(verbose_name='Doctor Description')
    birthday = models.DateField(verbose_name='Doctor Birthday')
    experience = models.PositiveSmallIntegerField(
        verbose_name='Doctor Experience')
    sort_number = models.PositiveBigIntegerField(
        verbose_name='Doctor Sort Number')
