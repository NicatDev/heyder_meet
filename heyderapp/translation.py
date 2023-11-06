from modeltranslation.translator import TranslationOptions,register, translator
from heyderapp.models import InMemory,Article,Blog,HomeHeader,HomeHeaderVideo,Video,Photo,Tag,Category,Movie,About,AllHeader,Interview





class AboutTranslationOptions(TranslationOptions):
    fields = ('minititle', 'title', 'content','content2','contentbig')


translator.register(About, AboutTranslationOptions)

class VideoTranslationOptions(TranslationOptions):
    fields = ('name', 'content','coverimage')


translator.register(Video, VideoTranslationOptions)
translator.register(InMemory, VideoTranslationOptions)

class MovieTranslationOptions(TranslationOptions):
    fields = ('name', 'content')


translator.register(Movie, MovieTranslationOptions)

class PhotoTranslationOptions(TranslationOptions):
    fields = ('name', 'content')


translator.register(Photo, PhotoTranslationOptions)


class HomeHeaderTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(HomeHeader, HomeHeaderTranslationOptions)


class AllHeaderTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(AllHeader, AllHeaderTranslationOptions)

class HomeHeaderVideoTranslationOptions(TranslationOptions):
    fields = ('name', 'coverimage')


translator.register(HomeHeaderVideo, HomeHeaderVideoTranslationOptions)

    
    
class BlogTranslationOptions(TranslationOptions):
    fields = ('name','content','content_without_ck', 'sidename','sidecontent','bottomname','bottomcontent')


translator.register(Blog, BlogTranslationOptions)

class ArticleTranslationOptions(TranslationOptions):
    fields = ('name','content')


translator.register(Article,ArticleTranslationOptions)
translator.register(Interview,ArticleTranslationOptions)
    
