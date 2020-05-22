from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class System(models.Model):
    name = models.CharField(max_length=20, verbose_name='System')

    owner = models.ForeignKey(User, verbose_name='Owner', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Created Time')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = 'System'


class CodeImg(models.Model):
    code_name = models.CharField(max_length=200, verbose_name='Code')
    code_img = models.ImageField(verbose_name='Code Image')

    def photo_url(self):
        if self.code_img and hasattr(self.code_img, 'url'):
            return self.code_img.url
        else:
            return '/default/1.jpg'

    def __str__(self):
        return self.code_name

    class Meta:
        verbose_name = verbose_name_plural = 'Code IMG'


class DriveType(models.Model):
    DRIVE_6X4 = 1
    DRIVE_6X2 = 2
    DRIVE_4X2 = 3
    DRIVE_TYPE = (
        (DRIVE_6X4, '6X4'),
        (DRIVE_6X2, '6X2'),
        (DRIVE_4X2, '4X2'),
    )
    name = models.PositiveIntegerField(choices=DRIVE_TYPE, verbose_name='Drive Type')
    owner = models.ForeignKey(User, verbose_name='Owner', on_delete=models.CASCADE, default=2)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Created Time')

    def __str__(self):
        return self.get_name_display()

    class Meta:
        verbose_name = verbose_name_plural = 'Drive Type'


class Packages(models.Model):
    COMFORT_CLASSIC = 10
    COMFORT_TOP = 11
    COMFORT_TOP_PLUS = 12
    DRIVER_OPERATION_CLASSIC = 20
    DRIVER_OPERATION_TOP = 21
    EFFICIENCY_CLASSIC = 30
    EXPRESS_CLASSIC = 40
    EXPRESS_TOP = 41
    SAFETY_TOP = 1
    MOUNTAIN = 2
    LIGHT_WEIGHT = 3
    ROAD_STAR = 4
    SUMMER_PACKAGE = 5
    WINTER_PACKAGE = 6

    PACKAGES_TYPE = (
        (COMFORT_CLASSIC, 'Comfort Classic'),
        (COMFORT_TOP, 'Comfort Top (only icw Comfort Classic)'),
        (COMFORT_TOP_PLUS, 'Comfort Top Plus (only icw Comfort Top)'),
        (DRIVER_OPERATION_CLASSIC, 'Driver Operation Classic'),
        (DRIVER_OPERATION_TOP, 'Driver Operation Top (only icw Operation Classic)'),
        (EFFICIENCY_CLASSIC, 'Efficiency Classic'),
        (EXPRESS_CLASSIC, 'Express Classic'),
        (EXPRESS_TOP, 'Express Top (only icw Express Classic)'),
        (SAFETY_TOP, 'Safety Top (only icw Express Top)'),
        (MOUNTAIN, 'Mountain'),
        (LIGHT_WEIGHT, 'Light Weight'),
        (ROAD_STAR, 'Road Star'),
        (SUMMER_PACKAGE, 'Summer Package (only icw Comfort Top)'),
        (WINTER_PACKAGE, 'Winter Package (only icw Comfort Classic)'),
    )
    name = models.PositiveIntegerField(choices=PACKAGES_TYPE, verbose_name='Packages')
    owner = models.ForeignKey(User, verbose_name='Owner', on_delete=models.CASCADE, default=2)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Created Time')

    def __str__(self):
        return self.get_name_display()

    class Meta:
        verbose_name = verbose_name_plural = 'Packages'


class CodesH6(models.Model):
    STATUS_ACTIVE = 1
    STATUS_DEACTIVE = 0
    STATUS_ITEMS = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_DEACTIVE, 'Deleted'),
    )

    H6A = 1
    H6B = 2
    H6 = 3
    NA = 0
    BRAND_ITEMS = (
        (H6A, 'H6A'),
        (H6B, 'H6B'),
        (H6, 'H6'),
        (NA, 'NA'),
    )

    name = models.CharField(max_length=10, verbose_name='Code')
    title = models.CharField(max_length=200, verbose_name='Title')
    system = models.ManyToManyField(System, verbose_name='System')
    comments = models.CharField(max_length=300, verbose_name='Comments', blank=True)
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, verbose_name='Status')
    restriction_with = models.CharField(max_length=500, verbose_name='With', blank=True)
    restriction_not_with = models.CharField(max_length=500, verbose_name='Not With', blank=True)
    brand = models.PositiveIntegerField(choices=BRAND_ITEMS, verbose_name='Brand', blank=True)
    drive_type = models.ManyToManyField(DriveType, verbose_name='Drive Type', blank=True)
    package = models.ManyToManyField(Packages, verbose_name='Package', blank=True)
    brief = RichTextUploadingField(blank=True, verbose_name='In Brief')
    benefits = RichTextUploadingField(blank=True,verbose_name='Benefits and Arguments')
    personal_comments = RichTextUploadingField(blank=True, verbose_name='Personal Comments')
    knowledge = RichTextUploadingField(blank=True, verbose_name='Knowledge')

    owner = models.ForeignKey(User, verbose_name='Owner', on_delete=models.CASCADE, default=3)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Created Time')

    def __str__(self):
        return self.name + '-' + self.title

    class Meta:
        verbose_name = verbose_name_plural = 'H6 Codes'




