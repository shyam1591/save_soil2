from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Represents a blog post
    """
    title = models.CharField(max_length=255, default="SAVE SOIL")
    content = models.TextField()
    author = models.TextField(default = "Shyam Mistry")
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save
    status = models.TextField(default="draft")
    published = models.TextField()
    slug = models.SlugField(default = "save-soil")
    topic = models.TextField()

    class Meta:
        """Sort by the `created` field. The `-` prefix
         specifies to order in descending/reverse order.
        Otherwise, it will be in ascending order."""
        ordering = ['created']

    def __str__(self):
        return self.title

class Topic(models.Model):
    name = models.CharField(max_length=255, default="Soil Importance")
    slug = models.SlugField(default = "soil-importance")

    def __str__(self):
        return self.name

class Comment(models.Model):
    post= models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=80)
    email=models.EmailField()
    text=models.TextField()
    approved=models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    
    class Meta:
        """Sort by the `created` field. The `-` prefix
         specifies to order in descending/reverse order.
        Otherwise, it will be in ascending order."""
        ordering = ['-created']