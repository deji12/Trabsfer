from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):

    title = models.CharField(max_length=225)
    thumbnail = models.FileField(upload_to="transfer/", null=True, blank=True)
    number_of_comments = models.IntegerField(default=0)
    content = RichTextField()
    published = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True, max_length=225)
    date = models.DateField(auto_now_add=True)

    def get_thumbnail(self) :
        if self.thumbnail and isinstance(self.thumbnail, models.fields.files.FieldFile):
            return self.thumbnail.url
        else:
            return ''
        
    def get_comments(self):
        return Comment.objects.filter(post=self)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    website = models.CharField(max_length=225, null=True, blank=True)
    content = models.TextField()
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name