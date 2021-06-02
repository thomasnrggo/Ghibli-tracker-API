from django.contrib import admin
from show_movies.models import Movies, Ratings, Profiles

admin.site.register(Movies)
admin.site.register(Ratings)


@admin.register(Profiles)
class ProfileAdmin(admin.ModelAdmin):
    pass