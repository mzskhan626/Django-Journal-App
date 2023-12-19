from django.contrib import admin

# Register your models here.
from .models import Topic
admin.site.register(Topic)
from .models import Topic, Entry
admin.site.register(Entry)