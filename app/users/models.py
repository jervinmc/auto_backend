from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin)
from django.utils import timezone
from .managers import CustomUserManager
import uuid

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    MALE='Male'
    USERNAME_FIELD = 'email'
    FEMALE='Female'
    GENDER=[(MALE, "Male"),(FEMALE, "Female")]
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_(
        'Designates whether the user can log into this admin site.'),blank=True)
    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this user should be treated as active. '
        'Unselect this instead of deleting accounts.'
    ),blank=True)
    date_joined = models.DateTimeField(
        _('date_joined'), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True,blank=True)
    name=models.CharField(_('name'),max_length=255,blank=True)
    firstname=models.CharField(_('firstname'),max_length=255,blank=True)
    lastname=models.CharField(_('lastname'),max_length=255,blank=True)
    middlename=models.CharField(_('middlename'),max_length=255,blank=True)
    contact_number=models.CharField(_('contact_number'),max_length=255,blank=True)
    descriptions=models.CharField(_('descriptions'),max_length=255,blank=True)
    address=models.CharField(_('address'),max_length=255,blank=True)
    username=models.CharField(_('username'),max_length=255,blank=True)
    age=models.CharField(_('age'),max_length=255,blank=True)
    gender=models.CharField(_('gender'),max_length=255,blank=True)
    suffix=models.CharField(_('suffix'),max_length=255,blank=True)
    occupation=models.CharField(_('occupation'),max_length=255,blank=True)
    password=models.CharField(_('password'),max_length=255,blank=True)
    email=models.CharField(_('email'),max_length=255,blank=True,unique=True)
    civil_status=models.CharField(_('civil_status'),max_length=255,blank=True)
    star_5=models.IntegerField(_('star_5'),blank=True,default=0)
    star_4=models.IntegerField(_('star_4'),blank=True,default=0)
    star_3=models.IntegerField(_('star_3'),blank=True,default=0)
    star_2=models.IntegerField(_('star_2'),blank=True,default=0)
    star_1=models.IntegerField(_('star_1'),blank=True,default=0)
    is_verified=models.BooleanField(_('is_verified'),default=True)
    account_type=models.CharField(_('account_type'),max_length=255,blank=True)
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/users_placeholder.png")
    payslip = models.ImageField(
        _('payslip'), upload_to=nameFile, default="uploads/users_placeholder.png")
    signed_image = models.ImageField(
        _('signed_image'), upload_to=nameFile, default="uploads/users_placeholder.png")
    car_price=models.CharField(_('car_price'),max_length=255,blank=True)
    location=models.CharField(_('location'),max_length=255,blank=True)
    car_transmission=models.CharField(_('car_transmission'),max_length=255,blank=True)
    mailing_address=models.CharField(_('mailing_address'),max_length=255,blank=True)
    name_signed=models.CharField(_('name_signed'),max_length=255,blank=True)
    city_of=models.CharField(_('city_of'),max_length=255,blank=True)
    state_of=models.CharField(_('state_of'),max_length=255,blank=True)
    car_brand=models.CharField(_('car_brand'),max_length=255,blank=True)
    car_category=models.CharField(_('car_category'),max_length=255,blank=True)
    car_color=models.CharField(_('car_color'),max_length=255,blank=True)
    objects = CustomUserManager()
    def __str__(self):
        return '{}'.format(self.email)  

    class Meta:
        ordering = ["-id"]
