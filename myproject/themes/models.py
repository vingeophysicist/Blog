from django.db import models
from mezzanine.pages.models import Page



# Create your models here.
class Quotes(Page):
    quotes_text = models.TextField()
    def __str__(self):
        return self.quotes_text
         

class Detail_quotes(models.Model):
    quotes = models.ForeignKey("Quotes")
    quotes_pics = models.ImageField(upload_to="quote")

    



    
