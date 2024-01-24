from .models import Post
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

@receiver(post_save, sender=Post)
def set_slug(sender, instance, created, **kwargs):
    if created and not instance.slug:
        # Check if it's a new instance and slug is not set
        instance.slug = slugify(instance.title)
        instance.save()