from django.contrib import admin

from .models import postClass
from .models import replayClass

admin.site.register(postClass)
admin.site.register(replayClass)
