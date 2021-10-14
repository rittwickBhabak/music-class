from .models import Song
from django.contrib import admin
admin.site.site_header = 'Songs Admin'
admin.site.site_title = 'Songs Admin Area'
admin.site.index_title = 'Welcome to the Songs admin area'
# Register your models here.
admin.site.register(Song)