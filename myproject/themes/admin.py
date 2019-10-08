from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Quotes
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost


# Register your models here.


admin.site.register(Quotes, PageAdmin)




