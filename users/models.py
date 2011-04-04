from django.db import models

class Group (models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()

class Person(models.Model):
    name = models.CharField(max_length=50)
    middlename = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    picture = models.URLField(verify_exists=True,max_length=100)	#class FileField(upload_to=None[, max_length=100, **options]) DA ERROR
    phonenumber = models.IntegerField(max_length=9)    
    email = models.EmailField(max_length=75)				#autovalida que tenga estructura de email
    birthday = models.DateTimeField()
    registerDay = models.DateField(auto_now_add=True)
    lastmodified = models.DateField(auto_now=True)	
    notes = models.TextField()
    website = models.URLField(verify_exists=True,max_length=100)	#Comprueba que no de un 404
    nickname = models.CharField(max_length=30)
    groups = models.ManyToManyField(Group)

   #def __unicode__(self):
   #   return u'%s' % (self.name)


#Informacion sobre models http://docs.djangoproject.com/en/dev/ref/models/fields/#


