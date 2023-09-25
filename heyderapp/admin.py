from django.contrib import admin
from heyderapp.models import Article,Blog,HomeHeader,HomeHeaderVideo,Video,Photo,Tag,Category,Movie
# Register your models here.
from ckeditor.widgets import CKEditorWidget
from django.db import models
class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(config_name='default')},
    }
admin.site.register(HomeHeader)
admin.site.register(HomeHeaderVideo)
admin.site.register(Article)
admin.site.register(Blog,MyModelAdmin)
admin.site.register(Video)
admin.site.register(Photo)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Movie)