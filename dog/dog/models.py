from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone

############
# DOG MODELS
############

########################################################################
# BOOKINGS
########################################################################
'''class Booking(models.Model):
    
    # WIP - NOT READY TO BE MIGRATED YET [NEEDS TESTED]
    #cottage_id = models.IntegerField(blank=True, default=0)
    #bookedby  = models.IntegerField(blank=True, default=0)
    #datebookedon = models.DateTimeField(auto_now_add=True, blank=True)
    #datebookedfrom = models.DateTimeField(blank=True)
    #datebookedto = models.DateTimeField(blank=True)
'''
########################################################################
# REVIEWS / RATINGS
########################################################################

'''class Review(models.Model):

    # MIGRATE ON TUESDAY EVENING
    # cottage_id
    #cottage_id = models.IntegerField(blank=True, default=0)
    # user_id
    # comments
    # rating [1 to 10 maybe]

'''
########################################################################
# CONTACT - Data from a contact form submission
########################################################################

'''class Contact(models.Model):

    # MIGRATE ON TUESDAY EVENING
    #contact_name = models.CharField(max_length=50,blank=True) # first name
    #contact_email = models.EmailField(max_length=50,blank=True)
    #form_content = models.TextField(max_length=500, blank=True)
'''
########################################################################
# Profile extends the default user table
########################################################################

class UserProfile(models.Model):

    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    usertype = models.CharField(max_length=50,blank=True) # tourist, host, admin
    fname = models.CharField(max_length=50,blank=True) # first name
    lname = models.CharField(max_length=50,blank=True) # last name

    # drop down choices
    USER_TYPES = (
	('guest','Guest'),
	('host','Host'),
        ('admin','Admin'),
    )
    usertype = models.CharField(max_length = 100, choices = USER_TYPES)
    bio = models.TextField(max_length=500, blank=True) # bio of user
    
########################################################################
# Cottage
########################################################################
class Cottage(models.Model):

    # check this out and see if this is true for auto increment
    # https://stackoverflow.com/questions/21128899/how-to-make-an-auto-increment-integer-field-django

    host = models.ForeignKey(User)
    name = models.CharField(max_length=128,blank=True)
    addr1 = models.CharField(max_length=128,blank=True)
    addr2 = models.CharField(max_length=128,blank=True )
    addr3 = models.CharField(max_length=128, blank=True)
    postcode = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    sleeps = models.IntegerField(choices=[(x, x) for x in range(1, 32)], blank=True, default=0)
    price_from = models.IntegerField(blank=True, default=0)
    price_to = models.IntegerField(blank=True, default=0)

    # drop down choices for regions
    # [not exhaustive]
    REGION_TYPES = (
        ('aberdeenshire','Aberdeenshire'),
        ('argyll','Argyll'),
        ('ayrshire','Ayrshire'),
        ('dumfries-and-galloway','Dumfries & Galloway'),
        ('angus','Angus'),
        ('edinburgh','Edinburgh'),
        ('fife','Fife'),
        ('glasgow','Glasgow'),
        ('highlands','Highlands'),
        ('loch-lomond','Loch Lomond / Trossachs'),
        ('orkney','Orkney'),
        ('outer-hebrides','Outer Hebrides'),
        ('perthshire','Perthshire'),
        ('scottish-borders','Scottish Borders'),
        ('shetland','Shetland'),
    )
    
    region = models.CharField(max_length=128,choices = REGION_TYPES)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    picture = models.ImageField(upload_to='cottage_images', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Cottage, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'cottages'

    def __str__(self):
        return self.name
