from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field="username", verbose_name=_("author"))
    title = models.CharField(_("title"), max_length=255)
    content = models.TextField(_("content"))
    date_created = models.DateField(
        _("date_created"), auto_now_add=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field="username", verbose_name=_("author"))
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, to_field="id", verbose_name=_("post"))
    date_created = models.DateField(
        _("date_created"), auto_now_add=True)

    def __str__(self):
        return self.post.title

    def __str__(self):
        return self.post.title
