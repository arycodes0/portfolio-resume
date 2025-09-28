import django
from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField

def get_url_image(instance, filename):
    return 'img/projects/%s' % (filename)


def get_url_tech_logo(instance, filename):
    return 'img/tech_logos/%s' % (filename)


class TechCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(
        default=0, help_text="Order for display")
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Tech(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    logo = ProcessedImageField(upload_to=get_url_tech_logo, format='webp')
    alt = models.CharField(max_length=50, blank=True, null=True)
    visible = models.BooleanField(default=False)
    category = models.ForeignKey(TechCategory,
                                 on_delete=models.CASCADE, related_name='technologies', blank=True, null=True)
    order = models.PositiveIntegerField(
        default=0, help_text="Order for display")

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.TextField(max_length=55)
    image = ProcessedImageField(upload_to=get_url_image, format='webp')
    github_url = models.URLField(
        max_length=200, blank=True, null=True, help_text="GitHub repository URL")
    live_demo_url = models.URLField(
        max_length=200, blank=True, null=True, help_text="Live demo URL")
    # medium = models.ImageField(upload_to=get_url_medium,blank=True)
    # medium = models.ImageField(upload_to=get_url_medium,blank=True)
    alt = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=2000)
    technologies = models.ManyToManyField(
        Tech, blank=True, help_text="Technologies used in this project")
    submit_date = models.DateTimeField(('date/time submitted'),
                                       default=timezone.now)
    visible = models.BooleanField(default=False)
    order = models.PositiveIntegerField(
        default=0, help_text="Order for display")
    # objects = ProjectManager()

    def __str__(self):
        return "Projects"
