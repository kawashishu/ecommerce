from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }