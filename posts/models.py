from datetime import datetime

from django.db import models


class PostCategory(models.Model):
    """
    Model for post categories.
    """
    name = models.CharField('Name', max_length=200, null=False)
    description = models.TextField('Description', default="")

    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = 'Post Categories'
        indexes = [models.Index(fields=['id', 'name', 'description'])]

    def get_children(self):
        return Post.objects.filter(category=self.id)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Model for posts.
    """
    author = models.CharField('Author', max_length=100, null=False)
    avatar = models.ImageField('Avatar', default='details-author.jpg')
    heading = models.CharField('Heading', max_length=200, null=False)
    picture = models.ImageField('Picture', default='product-1.jpg')
    content = models.TextField('Content')
    created_at = models.DateTimeField('Created at', default=datetime.now)
    category = models.ForeignKey(to=PostCategory, verbose_name='Category', on_delete=models.CASCADE, default='', related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        app_label = 'posts'
        indexes = [models.Index(fields=['id', 'author', 'heading', 'picture', 'content', 'created_at', 'category_id', 'avatar'])]

    def __str__(self):
        return self.heading
