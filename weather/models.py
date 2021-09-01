from django.db import models

# Create your models here.
class City (models.Model):
   city_name = models.CharField(max_length=255, help_text='Enter City name to know the weather ')

   #Metadata
   class Meta :
       ordering = ['-id']
       verbose_name = 'city'
       verbose_name_plural = 'cities'

#    #Methods
#    def get_absolute_url(self):
#        return reverse('url', args=[args])

   def __str__(self):
       return self.city_name