from django.contrib import admin
from .models import Plants,Information,Image

admin.site.register(Plants)
admin.site.register(Information)
class ImageAdmin(admin.ModelAdmin):
  list_display = ['Species','image_name']

admin.site.register(Image,ImageAdmin)

