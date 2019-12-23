from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(default='default.jpg', upload_to='avatars')

    @property
    def followers(self):
        return Follow.objects.filter(who_is_followed=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(who_follows=self.user).count()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300: 
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()


class Follow(models.Model):
    following = models.ForeignKey(User, related_name="who_follows", on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name="who_is_followed", on_delete=models.CASCADE)
    follow_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.follow_time}'
