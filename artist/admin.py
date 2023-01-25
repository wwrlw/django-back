from django.contrib import admin
from .models import Artist
from import_export.admin import ImportExportModelAdmin



class ArtistAdmin(ImportExportModelAdmin, admin.ModelAdmin, ):
    # list_display_links= ('title', 'createDate',)
    # list_display=( 'title','createDate',)
    list_filter = ('group',)
    search_fields = ('nickname',)
    # filter_horizontal = ('genre','timetable','place',)
    
    


admin.site.register(Artist, ArtistAdmin)
