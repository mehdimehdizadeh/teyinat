from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse

# Create your views here.

from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse,get_object_or_404,reverse
from .models import *
from django.core import mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    keyword = request.GET.get("keyword")
    sosial = sosials.objects.all()
    categories = Category.objects.all()
    if keyword:
        dey = "Axtarışn nəticəsi"
        s = 0
        article = Article.objects.filter(title__contains = keyword)
        for i in article:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        return render(request,"mostread.html",{"posts":article,"categories":categories,"sosial":sosial,"dey":dey})
    categories = Category.objects.all()
    last_posts = Article.objects.all()[:4]
    count = Article.objects.all()
    r = 0
    l = 0
    c = 0
    for i in count:
        r = r + i.comment_count
        l = l + i.like
        c = c + i.view
    posts = Article.objects.all().order_by('-view')[:4]
    context = {
        "categories":categories,
        "last_posts":last_posts,
        "sosial":sosial,
        "posts":posts,
        "r":r,
        "l":l,
        "c":c,
    }
    return render(request,'index.html',context)

def blog(request,id):
    keyword = request.GET.get("keyword")
    sosial = sosials.objects.all()
    categories = Category.objects.all()
    if keyword:
        dey = "Axtarışn nəticəsi"
        s = 0
        article = Article.objects.filter(title__contains = keyword)
        for i in article:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        return render(request,"mostread.html",{"posts":article,"categories":categories,"sosial":sosial,"dey":dey})
    cate = get_object_or_404(Category,id=id)
    post_lists = Article.objects.filter(category = cate)
    paginator = Paginator(post_lists,12)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    categories = Category.objects.all()
    sosial = sosials.objects.all()
    context = {
        "categories":categories,
        "posts":posts,
        "sosial":sosial,
        "cate":cate,
    }
    return render(request,'blog.html',context)

def sub_blog(request,id):
    keyword = request.GET.get("keyword")
    sosial = sosials.objects.all()
    categories = Category.objects.all()
    if keyword:
        dey = "Axtarışn nəticəsi"
        s = 0
        article = Article.objects.filter(title__contains = keyword)
        for i in article:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        return render(request,"mostread.html",{"posts":article,"categories":categories,"sosial":sosial,"dey":dey})
    sub_cate = get_object_or_404(Subcategory,id=id)
    cate = Category.objects.filter(subcategory = sub_cate)
    post_lists = Article.objects.filter(subcategory = sub_cate)
    paginator = Paginator(post_lists,12)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    categories = Category.objects.all()
    sosial = sosials.objects.all()
    context = {
        "categories":categories,
        "posts":posts,
        "sosial":sosial,
        "cate":cate,
        "sub_cate":sub_cate,
    }
    return render(request,'sub_blog.html',context)

def blog_user(request,id):
    keyword = request.GET.get("keyword")
    sosial = sosials.objects.all()
    categories = Category.objects.all()
    if keyword:
        dey = "Axtarışn nəticəsi"
        s = 0
        article = Article.objects.filter(title__contains = keyword)
        for i in article:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        return render(request,"mostread.html",{"posts":article,"categories":categories,"sosial":sosial,"dey":dey})
    user_name = get_object_or_404(user,id=id)
    post_lists = Article.objects.filter(user = user_name)
    paginator = Paginator(post_lists,12)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    sosial = sosials.objects.all()
    categories = Category.objects.all()
    context = {
        "sosial":sosial,
        "categories":categories,
        "posts":posts,
        "user_name":user_name,
    }
    return render(request,'blog-user.html',context)

def blog_single(request,slug):
    keyword = request.GET.get("keyword")
    sosial = sosials.objects.all()
    categories = Category.objects.all()
    if keyword:
        dey = "Axtarışn nəticəsi"
        s = 0
        article = Article.objects.filter(title__contains = keyword)
        for i in article:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        return render(request,"mostread.html",{"posts":article,"categories":categories,"sosial":sosial,"dey":dey})    
    sosial = sosials.objects.all()
    categories = Category.objects.all()
    post = get_object_or_404(Article,slug=slug)
    post.view = post.view + 1
    post.save()
    comments = post.comments.all()
    context = {
        "post":post,
        "comments":comments,
        "categories":categories,
        "sosial":sosial,
    }
    return render(request,'blog-single.html',context)

def blog_like(request,slug):
    keyword = request.GET.get("keyword")
    sosial = sosials.objects.all()
    categories = Category.objects.all()
    if keyword:
        dey = "Axtarışn nəticəsi"
        s = 0
        article = Article.objects.filter(title__contains = keyword)
        for i in article:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        return render(request,"mostread.html",{"posts":article,"categories":categories,"sosial":sosial,"dey":dey})
    sosial = sosials.objects.all()
    categories = Category.objects.all()
    post = get_object_or_404(Article,slug=slug)
    post.like = post.like + 1
    post.save()
    context = {
        "post":post,
        "categories":categories,
        "sosial":sosial,
    }
    return render(request,'blog-single.html',context)

def comment(request,slug):
    article = get_object_or_404(Article,slug = slug)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article = article
        newComment.save()
        article.comment_count += 1
        article.save()
    return redirect("/posts/"+article.slug)

def send_mail(request,id):
    subs = subscribe.objects.all()
    connection = mail.get_connection()
    connection.open()
    post = get_object_or_404(Article,id=id)
    for i in subs:
        text = "Bizim "+ "'"+ post.title + "'"+ " adlı məqaləmizlə tanış olmaq üçün linkə toxunun: " + "https://teyinat.com/posts/"+ post.slug
        email = mail.EmailMessage(
            post.title,
            text,
            'teyinat.user@gmail.com',
            [i.gmail]
        )
        connection.send_messages([email])
    connection.close()
    return redirect("/posts/"+post.slug)

def subscribe_site(request):
    subs = subscribe.objects.all()
    s = 0
    if request.method == "POST":
        mailing = request.POST.get("mail")
        for i in subs:
            if mailing == i.gmail:
                s = s + 1
        if s==0:
            newSubs = subscribe(gmail = mailing)
            newSubs.save()
    return redirect('index')

def lastpost(request):
    keyword = request.GET.get("keyword")
    sosial = sosials.objects.all()
    categories = Category.objects.all()
    if keyword:
        dey = "Axtarışn nəticəsi"
        s = 0
        article = Article.objects.filter(title__contains = keyword)
        for i in article:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        return render(request,"mostread.html",{"posts":article,"categories":categories,"sosial":sosial,"dey":dey})
    posts = Article.objects.all()[:12]
    categories = Category.objects.all()
    sosial = sosials.objects.all()
    context = {
        "categories":categories,
        "posts":posts,
        "sosial":sosial,
    }
    return render(request,'lastpost.html',context)

def mostread(request):
    keyword = request.GET.get("keyword")
    sosial = sosials.objects.all()
    categories = Category.objects.all()
    if keyword:
        dey = "Axtarışn nəticəsi"
        s = 0
        article = Article.objects.filter(title__contains = keyword)
        for i in article:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        return render(request,"mostread.html",{"posts":article,"categories":categories,"sosial":sosial,"dey":dey})
    posts = Article.objects.all().order_by('-view')[:12]
    categories = Category.objects.all()
    sosial = sosials.objects.all()
    context = {
        "categories":categories,
        "posts":posts,
        "sosial":sosial,
    }
    return render(request,'mostread.html',context)

def statistic(request):
    keyword = request.GET.get("keyword")
    sosial = sosials.objects.all()
    categories = Category.objects.all()
    if keyword:
        dey = "Axtarışn nəticəsi"
        s = 0
        article = Article.objects.filter(title__contains = keyword)
        for i in article:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        return render(request,"mostread.html",{"posts":article,"categories":categories,"sosial":sosial,"dey":dey})
    categories = Category.objects.all()
    count = Article.objects.all()
    r = 0
    l = 0
    c = 0
    for i in count:
        r = r + i.comment_count
        l = l + i.like
        c = c + i.view
    sosial = sosials.objects.all()
    context = {
        "categories":categories,
        "sosial":sosial,
        "r":r,
        "l":l,
        "c":c,
    }
    return render(request,'statistic.html',context)

def about(request):
    keyword = request.GET.get("keyword")
    sosial = sosials.objects.all()
    categories = Category.objects.all()
    if keyword:
        dey = "Axtarışn nəticəsi"
        s = 0
        article = Article.objects.filter(title__contains = keyword)
        for i in article:
            s += 1
        if s == 0:
            dey = "Çox təəssüf, belə bir məlumat yoxdur!"
        return render(request,"mostread.html",{"posts":article,"categories":categories,"sosial":sosial,"dey":dey})
    categories = Category.objects.all()
    sosial = sosials.objects.all()
    context = {
        "categories":categories,
        "sosial":sosial,
    }
    return render(request,'about.html',context)

def contact_admin(request):
    categories = Category.objects.all()
    sosial = sosials.objects.all()
    context = {
        "categories":categories,
        "sosial":sosial,
    }
    if request.method == "POST":
        name = request.POST.get("name")
        gmail = request.POST.get("gmail")
        phone = request.POST.get("phone")
        content = request.POST.get("content")
        newSubs = contact(name=name,gmail=gmail,phone=phone,content=content)
        newSubs.save()
        text = "Mesajınız göndərildi"
        context = {
        "categories":categories,
        "sosial":sosial,
        "text":text,
        }
        return render(request,'contact.html',context)

    return render(request,'contact.html',context)
