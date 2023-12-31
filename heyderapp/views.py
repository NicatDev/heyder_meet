from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from heyderapp.models import *
from django.urls import translate_url
from django.db.models import Q,F,FloatField,Count
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Count
from django.conf import settings

def embed(url):
    try:
        b = url.find('src="')
        if b != -1:
            e = url.find('"', b + 5)  
            if e != -1:
                src = url[b + 5:e]
        return src
    except:
        return ''
def set_language(request, lang_code):
    url = request.META.get("HTTP_REFERER", None)
    if lang_code == 'az':
        return HttpResponseRedirect('/')
    else:
        response = redirect(translate_url(url, lang_code))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        return response
    
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
   

    blog_list = paginator.get_page(page)
    if end > blog_list.number:
        end = blog_list.number

    
    most_blogs = Blog.objects.all().order_by('views')[0:3]
    tags = Tag.objects.annotate(blog_count = Count('blog'))
    if len(most_blogs)>4:
        most_blogs=most_blogs[0:4]
    allheader = AllHeader.objects.all()
    if allheader.exists():
        allheader = allheader.first()
    context = {
        'blog_list':blog_list,
        'tags':tags,
        'most_blogs':most_blogs,
        'start':start,
        'end':end,
        'iterator':range(start,end+1),
        'allheader':allheader
    }
    if Head.objects.all().exists():
        head = Head.objects.first()
        context['head'] = head
        
    context['current_tag']=tag_name

    if 1 in [x for x in range(start,end+1)]:
        context['pagcheck']='1'
    return render(request,'blog.html',context)

def article2(request):
    articles = Article.objects.all()
    tag_name = request.GET.get('tag','')
    if tag_name:
        articles = articles.filter(tag__name = tag_name)
    paginator = Paginator(articles, 1)
    page = request.GET.get("page", 1)
    article_list = paginator.get_page(page)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    fotcategories = Category.objects.annotate(photo_count=Count('fotolar')).filter(photo_count__gt=0)
    vidcategories = Category.objects.annotate(photo_count=Count('videolar')).filter(photo_count__gt=0)
    artcategories = Category.objects.annotate(photo_count=Count('meqaleler')).filter(photo_count__gt=0)
    allheader = AllHeader.objects.all()
    if allheader.exists():
        allheader = allheader.first()
    interviews = Interview.objects.all()
    books =  Book.objects.all()
    sourcearticles = AnotherSourceArticles.objects.all()
    context = {
        'articles':article_list,
        'fotcategories':fotcategories,
        'artcategories':artcategories,
        'vidcategories':vidcategories,
        'allheader':allheader,
        'interviews':interviews,
        'books':books,
        'sourcearticles':list(sourcearticles.values())
        }
    if Head.objects.all().exists():
        head = Head.objects.first()
        context['head'] = head
    return render(request,'article.html',context)

def article3(request):
    articles = InMemory.objects.filter(video_or_not=False)
    articless = InMemory.objects.filter(video_or_not=True)
    for x in articless:
        x.embed_full = embed(x.embed)
    for video in articless:
        video.embed_full = embed(video.embed)
    paginator = Paginator(articles, 12)
    page = request.GET.get("page", 1)
    article_list = paginator.get_page(page)
    paginatorr = Paginator(articless, 12)
    pages = request.GET.get("pages", 1)
    article_lists = paginatorr.get_page(pages)
  
    fotcategories = Category.objects.annotate(photo_count=Count('fotolar')).filter(photo_count__gt=0)
    vidcategories = Category.objects.annotate(photo_count=Count('videolar')).filter(photo_count__gt=0)
    artcategories = Category.objects.annotate(photo_count=Count('meqaleler')).filter(photo_count__gt=0)
    allheader = AllHeader.objects.all()
    interviews = Interview.objects.all()
    books =  Book.objects.all()
    sourcearticles = AnotherSourceArticles.objects.all()
    page_count = paginator.num_pages
    count = [count+1 for count in range(page_count)]
    if allheader.exists():
        allheader = allheader.first()
    sourcememories = AnotherSourceMemories.objects.all()

    product_count = len(sourcememories) 

    products_per_page = 6
    
    page_count = (product_count + products_per_page - 1) // products_per_page

    pagecount = [x+1 for x in range(page_count)]
    context = {
        'inmemories':article_list,
        'invideomemories':article_lists,
        'fotcategories':fotcategories,
        'artcategories':artcategories,
        'vidcategories':vidcategories,
        'allheader':allheader,
        'interviews':interviews,
        'books':books,
        'sourcememories':sourcememories,
        'count':count,
        'pagecount':pagecount

        
        }
    if Head.objects.all().exists():
        head = Head.objects.first()
        context['head'] = head
    context['video_list'] = Video.objects.all()
    return render(request,'xatireler.html',context)

def article(request):
    articles = Article.objects.all()
    searchmusahibe = request.GET.get('searchmusahibe','')
    searchmeqale = request.GET.get('searchmeqale','')

    if searchmeqale:
        articles = articles.filter(Q(name__icontains=searchmeqale) | Q(content__icontains=searchmeqale))
    
    paginator = Paginator(articles, 4)
    page = request.GET.get("page", 1)
    article_list = paginator.get_page(page)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    fotcategories = Category.objects.annotate(photo_count=Count('fotolar')).filter(photo_count__gt=0)
    vidcategories = Category.objects.annotate(photo_count=Count('videolar')).filter(photo_count__gt=0)
    artcategories = Category.objects.annotate(photo_count=Count('meqaleler')).filter(photo_count__gt=0)
    allheader = AllHeader.objects.all()
    interviews = Interview.objects.all()
    if searchmusahibe:
        interviews = interviews.filter(Q(name__icontains=searchmusahibe) | Q(content__icontains=searchmusahibe))
    paginator2 = Paginator(interviews, 4)
    page2 = request.GET.get("pages", 1)
    interview_list = paginator2.get_page(page2)
    books =  Book.objects.all()
    if allheader.exists():
        allheader = allheader.first()
    sourcearticles = AnotherSourceArticles.objects.all()
    sourceinterviews = AnotherSourceInterviews.objects.all()
    product_count = len(sourcearticles) 
    products_count = len(sourceinterviews)
    products_per_page = 6
    
    page_count = (product_count + products_per_page - 1) // products_per_page
    page_counts = (products_count + products_per_page - 1) // products_per_page
    pagecount = [x+1 for x in range(page_count)]
    pagecounts = [x+1 for x in range(page_counts)] 
    count = (len(articles)+3)//4
    count = [x+1 for x in range(count)]
    count2 = (len(interviews)+3)//4
    count2 = [x+1 for x in range(count2)]
    context = {
        'articles':article_list,
        'fotcategories':fotcategories,
        'artcategories':artcategories,
        'vidcategories':vidcategories,
        'allheader':allheader,
        'interviews':interview_list,
        'books':books,
        'sourcearticles':list(sourcearticles.values()),
        'sourceinterviews':list(sourceinterviews.values()),
        'pagecount':pagecount,
        'pagecounts':pagecounts,
        'count':count,
        'count2':count2
        }
    
    if Head.objects.all().exists():
        head = Head.objects.first()
        context['head'] = head
    return render(request,'article2.html',context)

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
    allheader = AllHeader.objects.all()
    if allheader.exists():
        allheader = allheader.first()
    context = {
        'blog':blog,
        'tags':tags,
        'alltags':Tag.objects.all(),
        'next':next_post,
        'pre':pre_post,
        'related_blogs':related_blogs,
        'most_blogs':most_blogs,
        'allheader':allheader
        
    }
    if Head.objects.all().exists():
        head = Head.objects.first()
        context['head'] = head
    return render(request,'blog-details.html',context)

def home(request):
    inmemories = InMemory.objects.all()
    fotcategories = Category.objects.annotate(photo_count=Count('fotolar')).filter(photo_count__gt=0)
    vidcategories = Category.objects.annotate(photo_count=Count('videolar')).filter(photo_count__gt=0)
    artcategories = Category.objects.annotate(photo_count=Count('meqaleler')).filter(photo_count__gt=0)

    if HomeHeader.objects.all().exists():
        homeHeader = HomeHeader.objects.all()[0]
    else:
        homeHeader = {}
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
    if len(videos)>6:
        videos = videos[0:6]
    for video in videos:
        video.embed_full = embed(video.embed)
        
    for video in homeHeaderVideo:
        video.embed_full = embed(video.embed)
    
    photos = Photo.objects.all().order_by('-created_at').filter(inhome=True)
    if len(photos)>11:
        photos = photos[0:14]
    if About.objects.all().exists():
        about = About.objects.first()
    else:
        about = {}
    testimonials = Testimonial.objects.all()
    partners = Partners.objects.all()    
    context = {'testimonials':testimonials,'partners':partners,'about':about,'artcategories':artcategories,'vidcategories':vidcategories,'fotcategories':fotcategories,'HomeHeader':homeHeader,'HomeHeaderVideo':homeHeaderVideo,'article1':article1,'article2':article2,'article3':article3,'blogs':blogs,'videos':videos,'photos':photos}
    if Head.objects.all().exists():
        head = Head.objects.first()
        context['head'] = head
    for video in inmemories:
        video.embed_full = embed(video.embed)
    if len(inmemories)>4:
        inmemories = inmemories[0:4]
    context['inmemories']=inmemories
    homeheader = HomeHeader.objects.exists()
    if homeheader:
        embed_code = embed(HomeHeader.objects.first().href)
    context['embed']=embed_code
    return render(request,'season-full.html',context)
# s
def video(request):
    allheader = AllHeader.objects.all()
    if allheader.exists():
        allheader = allheader.first()
    videos = Video.objects.all()
    cat = request.GET.get('movzu')
    if cat:
        videos = Video.objects.filter(category=cat)
    # movies = Movie.objects.all()
    paginator = Paginator(videos, 12)
    page = request.GET.get("page", 1)
    video_list = paginator.get_page(page)
    videos = videos.order_by('ordering')
    fotcategories = Category.objects.annotate(photo_count=Count('fotolar')).filter(photo_count__gt=0)
    vidcategories = Category.objects.annotate(photo_count=Count('videolar')).filter(photo_count__gt=0)
    artcategories = Category.objects.annotate(photo_count=Count('meqaleler')).filter(photo_count__gt=0)
    fcount = Video.objects.all().count()
    page_count = paginator.num_pages
    count = [count for count in range(page_count)]
    for video in video_list:
        video.embed_full = embed(video.embed)
  
    context = {
        'video_list':video_list,
        # 'movies':movies,
        # 'related_videos':videos,
        'categories':vidcategories,
        'fotcategories':fotcategories,
        'artcategories':artcategories,
        'vidcategories':vidcategories,
        'fcount':fcount,
        'allheader':allheader,
        'count':count
    }
    if Head.objects.all().exists():
        head = Head.objects.first()
        context['head'] = head
    return render(request,'video.html',context)

def foto(request):
    allheader = AllHeader.objects.all()
    if allheader.exists():
        allheader = allheader.first()
    fcount = Photo.objects.all().count()
    photos = Photo.objects.all().order_by('created_at')
    if request.GET.get('movzu'):
        photos = photos.filter(category=request.GET.get('movzu'))
    fotcategories = Category.objects.annotate(photo_count=Count('fotolar')).filter(photo_count__gt=0)
    vidcategories = Category.objects.annotate(photo_count=Count('videolar')).filter(photo_count__gt=0)
    artcategories = Category.objects.annotate(photo_count=Count('meqaleler')).filter(photo_count__gt=0)
# Get a queryset of categories with at least one product
    categories = Category.objects.annotate(photo_count=Count('fotolar')).filter(photo_count__gt=0)
    context = {
        'photos':photos,
        'categories':categories,
        'fcount':fcount,
        'fotcategories':fotcategories,
        'artcategories':artcategories,
        'vidcategories':vidcategories,
        'allheader':allheader
    }
    if Head.objects.all().exists():
        head = Head.objects.first()
        context['head'] = head
    return render(request,'foto.html',context)



def about(request):
    allheader = AllHeader.objects.all()
    if allheader.exists():
        allheader = allheader.first()
    if About.objects.all().exists():
        about = About.objects.first()
    else:
        about = {}
    
    fotcategories = Category.objects.annotate(photo_count=Count('fotolar')).filter(photo_count__gt=0)
    vidcategories = Category.objects.annotate(photo_count=Count('videolar')).filter(photo_count__gt=0)
    artcategories = Category.objects.annotate(photo_count=Count('meqaleler')).filter(photo_count__gt=0)
# Get a queryset of categories with at least one product
    categories = Category.objects.annotate(photo_count=Count('fotolar')).filter(photo_count__gt=0)
    context = {

        'categories':categories,
        'about':about,
        'fotcategories':fotcategories,
        'artcategories':artcategories,
        'vidcategories':vidcategories,
        'allheader':allheader
    }
    if Head.objects.all().exists():
        head = Head.objects.first()
        context['head'] = head
    return render(request,'about.html',context)




def articlesingle(request,slug=None):
    allheader = AllHeader.objects.all()
    if allheader.exists():
        allheader = allheader.first()
    blog = get_object_or_404(Article,slug=slug)
    
    if blog.date==None:
        blog.date = datetime.now()
        blog.save()
    next_post = Article.objects.filter(date__gt=blog.date).order_by('date').first()
    pre_post = Article.objects.filter(date__lt=blog.date).order_by('-date').first()
    if not next_post:
        next_post = Article.objects.exclude(slug=blog.slug)
        if next_post:
            next_post = next_post.first()
        else:
            next_post = blog
    if not pre_post:
        pre_post = Article.objects.exclude(slug=blog.slug).exclude(slug=next_post.slug)
        if pre_post:
            pre_post = pre_post.first()
        else:
            pre_post = blog
    
    tags = blog.tag.all()
    related_blogs = Article.objects.filter(tag__in=tags).exclude(slug=slug)# Adjust the number of related blogs as needed
    if related_blogs.exists():
        related_blogs = related_blogs[:3]
    
    if len(related_blogs)<2:
        related_blogs = (related_blogs | Article.objects.all()).distinct()[:3]
    most_blogs = Article.objects.all().order_by('views')[0:3]
    context = {
        'blog':blog,
        'tags':tags,
        'alltags':Tag.objects.all(),
        'next':next_post,
        'pre':pre_post,
        'related_blogs':related_blogs,
        'most_blogs':most_blogs,
        'allheader':allheader
        
    }
    if Head.objects.all().exists():
        head = Head.objects.first()
        context['head'] = head
    return render(request,'articlesingle.html',context)

def inmemorysingle(request,slug=None):
    allheader = AllHeader.objects.all()
    if allheader.exists():
        allheader = allheader.first()
    blog = get_object_or_404(InMemory,slug=slug)
    

    next_post = InMemory.objects.filter(created_at=blog.created_at).order_by('created_at').first()
    pre_post = InMemory.objects.filter(created_at__lt=blog.created_at).order_by('-created_at').first()
    if not next_post:
        next_post = InMemory.objects.exclude(slug=blog.slug)
        if next_post:
            next_post = next_post.first()
        else:
            next_post = blog
    if not pre_post:
        pre_post = InMemory.objects.exclude(slug=blog.slug).exclude(slug=next_post.slug)
        if pre_post:
            pre_post = pre_post.first()
        else:
            pre_post = blog
    
 
    related_blogs = InMemory.objects.filter().exclude(slug=slug)
    if related_blogs.exists():
        related_blogs = related_blogs[:3]
    # Adjust the number of related blogs as needed

    if len(related_blogs)<2:
        related_blogs = (related_blogs | InMemory.objects.all()).distinct()[:3]
    most_blogs = InMemory.objects.all()[0:3]
    context = {
        'blog':blog,
 
        'alltags':Tag.objects.all(),
        'next':next_post,
        'pre':pre_post,
        'related_blogs':related_blogs,
        'most_blogs':most_blogs,
        'allheader':allheader
        
    }
    if Head.objects.all().exists():
        head = Head.objects.first()
        context['head'] = head
    return render(request,'inmemory.html',context)

def interviewsingle(request,slug=None):
    allheader = AllHeader.objects.all()
    if allheader.exists():
        allheader = allheader.first()
    blog = get_object_or_404(Interview,slug=slug)
    
    if blog.date==None:
        blog.date = datetime.now()
        blog.save()
    next_post = Interview.objects.filter(date__gt=blog.date).order_by('date').first()
    pre_post = Interview.objects.filter(date__lt=blog.date).order_by('-date').first()
    if not next_post:
        next_post = Interview.objects.exclude(slug=blog.slug)
        if next_post:
            next_post = next_post.first()
        else:
            next_post = blog
    if not pre_post:
        pre_post = Interview.objects.exclude(slug=blog.slug).exclude(slug=next_post.slug)
        if pre_post:
            pre_post = pre_post.first()
        else:
            pre_post = blog
    
    tags = blog.tag.all()
    related_blogs = Interview.objects.filter(tag__in=tags).exclude(slug=slug)
    if related_blogs.exists():
        related_blogs = related_blogs[:3]
    # Adjust the number of related blogs as needed

    if len(related_blogs)<2:
        related_blogs = (related_blogs | Interview.objects.all()).distinct()[:3]
    most_blogs = Interview.objects.all().order_by('views')[0:3]
    context = {
        'blog':blog,
        'tags':tags,
        'alltags':Tag.objects.all(),
        'next':next_post,
        'pre':pre_post,
        'related_blogs':related_blogs,
        'most_blogs':most_blogs,
        'allheader':allheader
        
    }
    if Head.objects.all().exists():
        head = Head.objects.first()
        context['head'] = head
    return render(request,'interview.html',context)

def AnotherSourceView(request):
    data = list(AnotherSourceArticles.objects.all().values())  # Replace with your queryset
    return JsonResponse(data, safe=False)