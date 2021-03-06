from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    text = models.TextField(max_length=140)
    published_date = models.DateTimeField(blank=True, null=True)


    def published(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return '{}'.format(self.text[:10])


class Comment(models.Model):
    post = models.ForeignKey(Post, blank=True, related_name='posts_coments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(max_length=140)
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return '{}'.format(self.text[:10])


class Tag(models.Model):
    post = models.ManyToManyField(Post, blank=True, related_name='tags_posts')
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return '{}'.format(self.title)
