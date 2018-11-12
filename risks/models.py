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


class RiskField(models.Model):
    risk = models.ForeignKey(RiskType, related_name='fields', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)

    FIELD_TYPES = (
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('enum', 'Enum'),
    )
    field_type = models.CharField(max_length=16, choices=FIELD_TYPES)

    is_required = models.BooleanField(default=True)

    def __str__(self):
        return 'Field: {}, type: {}'.format(self.name, self.field_type)
