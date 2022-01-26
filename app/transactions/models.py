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


class Transactions(models.Model):
    user_id=models.CharField(_('user_id'),max_length=255,blank=True,null=True)
    label=models.CharField(_('label'),max_length=255,blank=True,null=True)
    customer_id=models.CharField(_('customer_id'),max_length=255,blank=True,null=True)
    customer_name=models.CharField(_('customer_name'),max_length=255,blank=True,null=True)
    image=models.CharField(_('image'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["-id"]
