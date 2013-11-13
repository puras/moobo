from django.contrib import admin

from bbs.models import Category, Node, Topic

# Register your models here.
admin.site.register(Category)
admin.site.register(Node)
admin.site.register(Topic)