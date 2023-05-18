import tomllib
import PIL
from django.db import models
from django.forms import ValidationError

def image_validation(image):
         config = tomllib.load('./config.toml')  
         img = PIL.Image.open(image)
         width, height = img.size
         if width > config['img_max_width'] or height > config['img_max_height']:
            raise ValidationError(f"Image dimensions must not exceed {config['img_max_width']}*{config['img_max_width'] } pixels.")

class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', validators=[image_validation])
    binary_image = models.BinaryField(null=True,blank=True)

    def __str__(self):
        return f"{self.title},{self.description},{self.image}"
    
