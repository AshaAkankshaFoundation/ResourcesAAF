from xxlimited import Null
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import Permission, User
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Contest(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField("Short Description",max_length=200, null=True)
    info = RichTextField("Information of Contest", null=True)
    image = CloudinaryField('image', null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.ManyToManyField(Category, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Submission(models.Model):
    user_id= models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_id")
    contest= models.ForeignKey(Contest,on_delete=models.CASCADE)
    caption=models.TextField(blank=True, null=True)
    likes=models.ManyToManyField(User, blank=True, null=True)
<<<<<<< HEAD
    image_url= models.TextField(blank=True, null=True)
    image_id=models.CharField(null=True,default=Null,max_length=200)
=======
    image= models.TextField(blank=True, null=True)
>>>>>>> 2dab8b20ec3ed570de0880481036402e041a79d7
    # video_url=models.TextField(blank=True, null=True)
    status=models.BooleanField(default=False)

