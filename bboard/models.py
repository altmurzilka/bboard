from django.db import models

# Create your models here.


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name="Item")
    content = models.TextField(null=True, blank=True, verbose_name="Description")
    price = models.FloatField(null=True, blank=True, verbose_name='Price')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')

    # objects = models.Manager()
    class Meta:
        verbose_name_plural = 'Notes'
        verbose_name = 'Note'
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Name')
    
    class Meta:
        verbose_name_plural = 'Headings'
        verbose_name = 'Heading'
        ordering = ['name']




