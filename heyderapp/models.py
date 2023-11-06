from django.db import models
from heyderapp.utils import create_slug_shortcode
from django.contrib.auth import get_user, get_user_model
from heyderapp.utils import *
from datetime import datetime
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=800)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=800)
    
    def __str__(self):
        return self.name

class BaseMixin(models.Model):
    slug = models.SlugField(unique=True,editable=False,blank=True,null=True)
    created_at = models.DateField(auto_now_add=True,blank=True,null=True,)
    title = models.CharField(max_length=1200,null=True,blank=True,verbose_name='title for seo')
    keyword = models.CharField(max_length=1200,null=True,blank=True,verbose_name='keyword for seo')
    alt = models.CharField(max_length=1200,null=True,blank=True)
    description = models.CharField(max_length=1200,null=True,blank=True,verbose_name='description for seo')
    
    class Meta:
        abstract = True
    
class About(models.Model):
    minititle = models.CharField(max_length=100)
    title = models.CharField(max_length=180) 
    content = models.CharField(max_length=3200)
    content2 =models.CharField(max_length=3200)
    contentbig = models.TextField()
    image = models.ImageField(verbose_name='690-732')   
    imza = models.CharField(max_length=120)
    
    def __str__(self):
        return self.title + 'Ana Sehife lahiye haqqinda'
    
    def save(self, *args, **kwargs):
        self.pk = 1  
        super(About, self).save(*args, **kwargs)
        
class Video(BaseMixin):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name='videolar')
    name = models.CharField(max_length=800)
    content = models.TextField()
    coverimage = models.ImageField()
    video = models.CharField(max_length=3200)
    ordering = models.IntegerField(null=True,blank=True)
    embed = models.CharField(max_length=4000,null=True,blank=True)
    
    def __str__(self):
        return self.name + ' -video'
    
    def save(self, *args, **kwargs):
        new_slug = slugify(self.name)
        self.slug = new_slug
        if Video.objects.filter(slug=new_slug).exists():
            count = 0
            while Video.objects.filter(slug=new_slug).exists():
                new_slug = f"{slugify(self.name)}-{count}"
                count += 1
        super(Video, self).save(*args, **kwargs)

class InMemory(BaseMixin):
    name = models.CharField(max_length=800)
    content = models.TextField()
    coverimage = models.ImageField()
    video = models.CharField(max_length=3200)
    ordering = models.IntegerField(null=True,blank=True)
    embed = models.CharField(max_length=4000,null=True,blank=True)
    
    def __str__(self):
        return self.name + ' -InMemory'
    
    def save(self, *args, **kwargs):
        new_slug = slugify(self.name)
        self.slug = new_slug
        if InMemory.objects.filter(slug=new_slug).exists():
            count = 0
            while InMemory.objects.filter(slug=new_slug).exists():
                new_slug = f"{slugify(self.name)}-{count}"
                count += 1
        super(InMemory, self).save(*args, **kwargs)

class Movie(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name='filmler')
    name = models.CharField(max_length=800)
    content = models.TextField()
    coverimage = models.ImageField()
    video = models.CharField(max_length=3400)
    ordering = models.IntegerField(null=True,blank=True)
    
    
    def __str__(self):
        return self.name + ' film'
    

class Photo(BaseMixin):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name='fotolar')
    name = models.CharField(max_length=800)
    content = models.TextField()
    image = models.ImageField()
    ordering = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.name + ' foto'
    
    def save(self, *args, **kwargs):
        new_slug = slugify(self.name)
        self.slug = new_slug
        if Photo.objects.filter(slug=new_slug).exists():
            count = 0
            while Photo.objects.filter(slug=new_slug).exists():
                new_slug = f"{slugify(self.name)}-{count}"
                count += 1
        super(Photo, self).save(*args, **kwargs)
    
class HomeHeader(models.Model):
    title = models.CharField(max_length=1200,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    href = models.CharField(max_length=1200,null=True,blank=True)
    video = models.FileField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return 'Ana Sehife Header '
    
    def save(self, *args, **kwargs):
        self.pk = 1  
        super(HomeHeader, self).save(*args, **kwargs)
        
class AllHeader(models.Model):
    title = models.CharField(max_length=1200)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    href = models.CharField(max_length=1200,null=True,blank=True)
    def __str__(self):
        return 'Diger Sehife Header '+self.title
    

    
class HomeHeaderVideo(models.Model):
    name = models.CharField(max_length=230)
    video = models.CharField(max_length=3400)
    coverimage = models.ImageField(null=True,blank=True)
    embed = models.CharField(max_length=4000,null=True,blank=True)
    def __str__(self):
        return 'Ana Sehife Header Video -' + self.name
    
class Blog(BaseMixin):
    tag = models.ManyToManyField(Tag,null=True,blank=True)
    name = models.CharField(max_length=1200,unique=True)
    content_without_ck = models.CharField(max_length=1200,null=True,blank=True)
    content = models.TextField()
    image = models.ImageField()
    date = models.DateField(null=True,blank=True)
    ordering = models.SmallIntegerField(null=True,blank=True)
    sidename = models.CharField(max_length=230,null=True,blank=True)
    sidecontent = models.TextField(null=True,blank=True)
    sideimage1 = models.ImageField(null=True,blank=True)
    sideimage2 = models.ImageField(null=True,blank=True)
    bottomname = models.CharField(max_length=1200,null=True,blank=True)
    bottomcontent = models.CharField(max_length=12000,null=True,blank=True)
    bottomimage = models.ImageField(null=True,blank=True)
    views = models.CharField(max_length=1000,null=True,blank=True,default=0)
    def __str__(self):
        return self.name +  ' xeber'
    
    def save(self, *args, **kwargs):
        new_slug = slugify(self.name)
        self.slug = new_slug
        if Blog.objects.filter(slug=new_slug).exists():
            count = 0
            while Blog.objects.filter(slug=new_slug).exists():
                new_slug = f"{slugify(self.name)}-{count}"
                count += 1
        super(Blog, self).save(*args, **kwargs)
  
    class Meta:
        verbose_name = "Xeber"
        verbose_name_plural = "Xeberler"
    
class Article(BaseMixin):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name='meqaleler')
    tag = models.ManyToManyField(Tag,null=True,blank=True)
    name = models.CharField(max_length=1200)
    date = models.DateField(null=True,blank=True)
    content = models.TextField()
    image = models.ImageField()
    views = models.CharField(max_length=12000,null=True,blank=True)
    def __str__(self):
        return self.name  + 'meqale'

    def save(self, *args, **kwargs):
        new_slug = slugify(self.name)
        self.slug = new_slug
        if Article.objects.filter(slug=new_slug).exists():
            count = 0
            while Article.objects.filter(slug=new_slug).exists():
                new_slug = f"{slugify(self.name)}-{count}"
                count += 1
        super(Article, self).save(*args, **kwargs)
        
class Interview(BaseMixin):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name='musahibeler')
    tag = models.ManyToManyField(Tag,null=True,blank=True)
    name = models.CharField(max_length=1200)
    date = models.DateField(null=True,blank=True)
    content = models.TextField()
    image = models.ImageField()
    views = models.CharField(max_length=12000,null=True,blank=True)
    
    def __str__(self):
        return self.name  + '--interview'

    def save(self, *args, **kwargs):
        new_slug = slugify(self.name)
        self.slug = new_slug
        if Interview.objects.filter(slug=new_slug).exists():
            count = 0
            while Interview.objects.filter(slug=new_slug).exists():
                new_slug = f"{slugify(self.name)}-{count}"
                count += 1
        super(Interview, self).save(*args, **kwargs)
        

class Partners(BaseMixin):
    name = models.CharField(max_length=1200)
    image = models.ImageField()
    
    def __str__(self):
        return self.name  + ' emekdas'
    
class Head(models.Model):
    title = models.CharField(verbose_name='head title',max_length=230)
    image = models.FileField(verbose_name='favicon',null=True,blank=True)
    logoheader = models.FileField(null=True,blank=True,verbose_name='diger_butun_loqolar')
    def __str__(self):
        return 'favicon'
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super(Head, self).save(*args, **kwargs)


class Testimonial(models.Model):
    full_name = models.CharField(max_length=120)
    field  = models.CharField(max_length=120)
    image = models.ImageField()
    title = models.CharField(max_length=230)
    decsription = models.TextField()
    
    def __str__(self):
        return self.full_name