from django.db import models
from django.utils.text import slugify


class RiskType(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(RiskType, self).save(*args, **kwargs)

    def __str__(self):
        return 'Risk type: {}'.format(self.name)
