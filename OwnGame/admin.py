from django.contrib import admin
from .models import *

admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Team)
admin.site.register(Leading)
admin.site.register(Match)
admin.site.register(MatchTeam)
admin.site.register(MatchQuestion)
