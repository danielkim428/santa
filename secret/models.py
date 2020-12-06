from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=5, null=True)
    start = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Letter(models.Model):
    date = models.DateTimeField(null=True)
    content = models.CharField(max_length=3000, blank=True, null=True)
    angel = models.ForeignKey(User, on_delete=models.CASCADE, related_name="letter_from", blank=True, null=True)
    mortal = models.ForeignKey(User, on_delete=models.CASCADE, related_name="letter_to", blank=True, null=True)

    def __str__(self):
        return '%s to %s' % (self.angel, self.mortal)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=3000, blank=True, null=True)
    mortal = models.OneToOneField(User, on_delete=models.CASCADE, related_name="angel_of", blank=True, null=True)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
     return self.user.username
