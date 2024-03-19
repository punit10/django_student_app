from django.contrib import admin
from score.models import Score

#to see the name and marks both in admin side
class ScoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'marks']

admin.site.register(Score, ScoreAdmin)