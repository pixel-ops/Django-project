from django.contrib import admin
from .models import mycontact,myabout,mypost,myregister,multiple_images
# Register your models here.

@admin.register(mypost)
class myPostAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    fields = (('topic','author'),'content',('content_type','genre'),'img')
    exclude = ('time','date')
    list_filter = ('author','genre')
    search_fields = ('author','genre')  



admin.site.register(mycontact)
admin.site.register(myabout)
admin.site.register(myregister)
admin.site.register(multiple_images)
# admin.site.register(mypost,myPostAdmin)
