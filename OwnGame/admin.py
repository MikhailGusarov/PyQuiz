from django.contrib import admin
from .models import Game, Category, SimpleQuestion

admin.site.register(Game)
admin.site.register(Category)
admin.site.register(SimpleQuestion)
