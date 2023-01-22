from django.contrib import admin
from authentication.models import User
from artist.models import Artist


admin.site.register(User)
admin.site.register(Artist)
# Register your models here.
