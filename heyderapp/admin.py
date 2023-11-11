from django.contrib import admin
from heyderapp.models import AnotherSourceMemories,AnotherSourceInterviews,AnotherSourceArticles,Book,Interview,InMemory,Testimonial,Head,Article,Blog,HomeHeader,HomeHeaderVideo,Video,Photo,Tag,Category,Movie,About,AllHeader,Partners
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

class MyNameAdmin222(admin.ModelAdmin):
    exclude = ('name','content','contentforall')
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(config_name='default')},
    }
class MyNameAdmin2(admin.ModelAdmin):
    exclude = ('name','content')
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(config_name='default')},
    }
admin.site.register(Interview,MyNameAdmin2)
class MyNameAdminVideo(admin.ModelAdmin):
    exclude = ('name','content','coverimage')
class MyNameAdminVideo2(admin.ModelAdmin):
    exclude = ('name','content','coverimage') 
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(config_name='default')},
    }
class MyNameAdminVideo3(admin.ModelAdmin):
    exclude = ('name','content','coverimage','interview') 
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(config_name='default')},
    }
class MyOnlyNameAdmin(admin.ModelAdmin):
    exclude = ('name','content','coverimage')
class BookAdmin(admin.ModelAdmin):
    exclude = ('name','writer')
class MyminiTitleAdmin(admin.ModelAdmin):
    exclude = ('minititle','title','content','content2','contentbig')
admin.site.register(HomeHeader,MyTitleAdmin)
admin.site.register(HomeHeaderVideo,MyOnlyNameAdmin)
admin.site.register(Article,MyNameAdmin222)

admin.site.register(Blog,MyModelAdmin)
admin.site.register(Video,MyNameAdminVideo)
admin.site.register(Photo,MyNameAdmin)
admin.site.register(Tag)

admin.site.register(Movie,MyOnlyNameAdmin)
admin.site.register(About,MyminiTitleAdmin)
admin.site.register(AllHeader,MyTitleAdmin)
admin.site.register(Partners)
admin.site.register(Head)
admin.site.register(Testimonial)
admin.site.register(InMemory,MyNameAdminVideo3)
admin.site.register(Book,BookAdmin)
admin.site.register(AnotherSourceArticles,MyTitleAdmin)
admin.site.register(AnotherSourceInterviews,MyTitleAdmin)
admin.site.register(AnotherSourceMemories,MyTitleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('name',) 

admin.site.register(Category,CategoryAdmin)