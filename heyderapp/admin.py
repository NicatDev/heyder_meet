from django.contrib import admin
from heyderapp.models import Article,Blog,HomeHeader,HomeHeaderVideo,Video,Photo,Tag,Category,Movie,About
# Register your models here.
from ckeditor.widgets import CKEditorWidget
from django.db import models
class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(config_name='default')},
    }
    exclude = ('content_without_ck','content','name','bottomcontent','sidename','sidecontent','bottomname')
class MyTitleAdmin(admin.ModelAdmin):
    exclude = ('title','content')
class MyNameAdmin(admin.ModelAdmin):
    exclude = ('name','content')
class MyOnlyNameAdmin(admin.ModelAdmin):
    exclude = ('name','content')
class MyminiTitleAdmin(admin.ModelAdmin):
    exclude = ('minititle','title','content','content2','contentbig')
admin.site.register(HomeHeader,MyTitleAdmin)
admin.site.register(HomeHeaderVideo,MyOnlyNameAdmin)
admin.site.register(Article,MyNameAdmin)
admin.site.register(Blog,MyModelAdmin)
admin.site.register(Video,MyNameAdmin)
admin.site.register(Photo,MyNameAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Movie,MyOnlyNameAdmin)
admin.site.register(About,MyminiTitleAdmin)