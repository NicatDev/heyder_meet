from django.shortcuts import render, redirect, get_object_or_404
from heyderapp.models import *
from django.db.models import Q,F,FloatField,Count
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Count


def meetjoin(request):
    context = {}
    return render(request,'index.html',context)

def blog(request):
    
    blogs = Blog.objects.all().order_by('ordering')
    if request.GET.get('blog'):
        name = request.GET.get('blog')
        blogs = blogs.filter(Q(name__icontains=name) | Q(content__icontains=name))
    tag_name = request.GET.get('tag','')
    if tag_name:
        blogs = blogs.filter(tag__name = tag_name)
        
    paginator = Paginator(blogs, 4)
    page = request.GET.get("page", 1)

    start = int(page)-3
    end = int(page)+3
    if start<1:
        start = 1
        end = end+3
   
    print(start,)
    blog_list = paginator.get_page(page)
    if end > blog_list.number:
        end = blog_list.number

    
    most_blogs = Blog.objects.all().order_by('views')[0:3]
    tags = Tag.objects.annotate(blog_count = Count('blog'))
    if len(most_blogs)>4:
        most_blogs=most_blogs[0:4]
    
    context = {
        'blog_list':blog_list,
        'tags':tags,
        'most_blogs':most_blogs,
        'start':start,
        'end':end,
        'iterator':range(start,end+1)
    }
  
        
    context['current_tag']=tag_name

    if 1 in [x for x in range(start,end+1)]:
        context['pagcheck']='1'
    return render(request,'blog.html',context)

def article(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 12)
    page = request.GET.get("page", 1)
    article_list = paginator.get_page(page)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    context = {'articles':article_list}
    return render(request,'article.html',context)

def blogsingle(request,slug=None):

    blog = get_object_or_404(Blog,slug=slug)
    next_post = Blog.objects.filter(date__gt=blog.date).order_by('date').first()
    pre_post = Blog.objects.filter(date__lt=blog.date).order_by('-date').first()
    if not next_post:
        next_post = Blog.objects.filter(date__lt=blog.date).order_by('-date').first()
    if not pre_post:
        pre_post = Blog.objects.filter(date__gt=blog.date).order_by('date').first()
    
    tags = blog.tag.all()
    related_blogs = Blog.objects.filter(tag__in=tags).exclude(slug=slug).distinct()[:3]  # Adjust the number of related blogs as needed
    if len(related_blogs)<2:
        related_blogs = (related_blogs | Blog.objects.all()).distinct()[:3]
    most_blogs = Blog.objects.all().order_by('views')[0:3]
    context = {
        'blog':blog,
        'tags':tags,
        'alltags':Tag.objects.all(),
        'next':next_post,
        'pre':pre_post,
        'related_blogs':related_blogs,
        'most_blogs':most_blogs
        
    }
    return render(request,'blog-details.html',context)

def home(request):
    fotcategories = Category.objects.annotate(photo_count=Count('fotolar')).filter(photo_count__gt=0)
    vidcategories = Category.objects.annotate(photo_count=Count('videolar')).filter(photo_count__gt=0)
    artcategories = Category.objects.annotate(photo_count=Count('meqaleler')).filter(photo_count__gt=0)
    if HomeHeader.objects.all().exists():
        homeHeader = HomeHeader.objects.all()[0]
    homeHeaderVideo = HomeHeaderVideo.objects.all()
    article = Article.objects.all()
    if article.exists():
        if len(article)==1:
            article1,article2,article3 =article[0],article[0],article[0]
        if len(article)==2:
            article1,article3 = article[0],article[0]
            article2 = article[1]
        if len(article)>2:
            article1 = article[0]
            article2 = article[1]
            article3 = article[2]
    else:
        article1,article2,article3 = {'name':'','image':{'url':''},'content':''}
        
    blogs = Blog.objects.all().order_by('ordering')
    if len(blogs)>3:
        blogs = blogs[0:3]
    videos = Video.objects.all()
    if len(videos)>3:
        videos = videos[0:3]
    photos = Photo.objects.all()
    if len(photos)>3:
        photos = photos[0:3]

    context = {'artcategories':artcategories,'vidcategories':vidcategories,'fotcategories':fotcategories,'HomeHeader':homeHeader,'HomeHeaderVideo':homeHeaderVideo,'article1':article1,'article2':article2,'article3':article3,'blogs':blogs,'videos':videos,'photos':photos}
    return render(request,'season-full.html',context)

def video(request):
    videos = Video.objects.all()
    cat = request.GET.get('movzu')
    if cat:
        videos = Video.objects.filter(category=cat)
    movies = Movie.objects.all()
    paginator = Paginator(videos, 12)
    page = request.GET.get("page", 1)
    video_list = paginator.get_page(page)
    videos = videos.order_by('ordering')
    vidcategories = Category.objects.annotate(video_count=Count('videolar')).filter(video_count__gt=0)
    context = {
        'video_list':video_list,
        'movies':movies,
        'related_videos':videos,
        'categories':vidcategories
    }
    return render(request,'video.html',context)

def foto(request):
    fcount = Photo.objects.all().count()
    photos = Photo.objects.all()
    if request.GET.get('movzu'):
        photos = photos.filter(category=request.GET.get('movzu'))

# Get a queryset of categories with at least one product
    categories = Category.objects.annotate(photo_count=Count('fotolar')).filter(photo_count__gt=0)
    context = {
        'photos':photos,
        'categories':categories,
        'fcount':fcount
    }
    return render(request,'foto.html',context)



