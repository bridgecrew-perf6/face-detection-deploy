from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class FaceRecognition(models.Model):
    id = models.AutoField(primary_key=True)
    record_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="Images/")
    
    class Meta:
        verbose_name_plural = "Face Recognitions"

    def  image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="100" height="50" />' % (self.image))

    image_tag.allow_tags = True

    def __str__(self):
        return str(self.id) + str(self.record_date)
    