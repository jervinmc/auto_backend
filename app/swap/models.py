from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Swap(models.Model):
    title=models.CharField(_('title'),max_length=255,blank=True,null=True)
    listing_id=models.CharField(_('code'),max_length=255,blank=True,null=True)
    user_id=models.CharField(_('name'),max_length=255,blank=True,null=True)
    name=models.CharField(_('name'),max_length=255,blank=True,null=True)
    milleage=models.CharField(_('milleage'),max_length=255,blank=True,null=True)
    color=models.CharField(_('color'),max_length=255,blank=True,null=True)
    category=models.CharField(_('category'),max_length=255,blank=True,null=True)
    fuel_type=models.CharField(_('fuel_type'),max_length=255,blank=True,null=True)
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/users_placeholder.png")
    class Meta:
        ordering = ["-id"]
