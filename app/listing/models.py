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



class Listing(models.Model):
    title=models.CharField(_('title'),max_length=255,blank=True,null=True)
    price=models.CharField(_('price'),max_length=255,blank=True,null=True)
    brand=models.CharField(_('brand'),max_length=255,blank=True,null=True)
    year=models.CharField(_('year'),max_length=255,blank=True,null=True)
    model=models.CharField(_('model'),max_length=255,blank=True,null=True)
    user_id=models.CharField(_('user_id'),max_length=255,blank=True,null=True)
    condition=models.CharField(_('condition'),max_length=255,blank=True,null=True)
    color=models.CharField(_('color'),max_length=255,blank=True,null=True)
    variant=models.CharField(_('variant'),max_length=255,blank=True,null=True)   
    body_type=models.CharField(_('body_type'),max_length=255,blank=True,null=True)
    fuel_type=models.CharField(_('fuel_type'),max_length=255,blank=True,null=True)
    category=models.CharField(_('category'),max_length=255,blank=True,null=True)
    milleage=models.CharField(_('milleage'),max_length=255,blank=True,null=True) 
    numberOfSeats=models.CharField(_('numberOfSeats'),max_length=255,blank=True,null=True) 
    current_bid=models.CharField(_('current_bid'),max_length=255,blank=True,null=True) 
    isBid = models.BooleanField(_('isBid'), default=False,blank=True)
    isSell = models.BooleanField(_('isSell'), default=False,blank=True)
    isSwap = models.BooleanField(_('isSwap'), default=False,blank=True)
    start_bidding=models.CharField(_('start_bidding'),max_length=255,blank=True,null=True)
    live_bidding=models.CharField(_('live_bidding'),max_length=255,blank=True,null=True)
    transmission=models.CharField(_('transmission'),max_length=255,blank=True,null=True)
    plate_number=models.CharField(_('plate_number'),max_length=255,blank=True,null=True)
    descriptions=models.CharField(_('descriptions'),max_length=255,blank=True,null=True)
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/users_placeholder.png")
    class Meta:
        ordering = ["-id"]
