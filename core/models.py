
from django.db import models
from django.utils.text import slugify
import os
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    live_demo_url = models.URLField(blank=True, null=True)
    source_code_url = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(upload_to='project_images/', blank=True)
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption or f"Extra image for {self.project.title}"

class Certificates(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='certificates/')
    thumbnail = models.ImageField(upload_to='certificate_thumbnails/', blank=True, null=True)

    def get_or_generate_thumbnail(self):
        from .utils import generate_thumbnail
        import os

        if self.thumbnail:
            return self.thumbnail.url  # ✅ Already generated

        if self.file and self.file.name.lower().endswith('.pdf'):
            thumb = generate_thumbnail(self.file.path)
            if thumb:
                name = os.path.splitext(os.path.basename(self.file.name))[0] + "_preview.jpg"
                self.thumbnail.save(name, thumb, save=True)
                return self.thumbnail.url
        return None
    def __str__(self):
        return self.title
    
class Skills(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
class Resume(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

