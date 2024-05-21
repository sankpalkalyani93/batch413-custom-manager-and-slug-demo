from django.db import models
from django.utils.text import slugify

# Create your models here.
class PersonActiveStateManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
    

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)

    active = PersonActiveStateManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(f"{self.first_name}")
            slug = original_slug
            counter = 1

            while Person.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter = counter + 1
            
            self.slug = slug
        super().save(*args, **kwargs)
        

    def __str__(self):
        return f"{self.first_name} {self.last_name}"