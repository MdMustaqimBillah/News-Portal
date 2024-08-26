from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from NewsApp.models import NewsArticle,Advertisement
from NewsApp.forms import AdvertisementForm
import uuid

# Create your views here.

def home(request):
    all_articles = NewsArticle.objects.all()
    main_article = NewsArticle.objects.filter(importance_level = 'main').first()
    r2c1_article = NewsArticle.objects.filter(importance_level = 'r2c1').first()
    r2c2_article = NewsArticle.objects.filter(importance_level = 'r2c2').first()
    r2c3_article = NewsArticle.objects.filter(importance_level = 'r2c3').first()
    r3c1_article = NewsArticle.objects.filter(importance_level = 'r3c1').first()
    r3c2_article = NewsArticle.objects.filter(importance_level = 'r3c2').first()
    r3c3_article = NewsArticle.objects.filter(importance_level = 'r3c3').first()
    r4c1_article = NewsArticle.objects.filter(importance_level = 'r4c1').first()
    r4c2_article = NewsArticle.objects.filter(importance_level = 'r4c2').first()
    r4c3_article = NewsArticle.objects.filter(importance_level = 'r4c3').first()
    r4c4_article = NewsArticle.objects.filter(importance_level = 'r4c4').first()
    r5c1_article = NewsArticle.objects.filter(importance_level = 'r5c1').first()
    r5c2_article = NewsArticle.objects.filter(importance_level = 'r5c2').first()
    r5c3_article = NewsArticle.objects.filter(importance_level = 'r5c3').first()
    r5c4_article = NewsArticle.objects.filter(importance_level = 'r5c4').first()
    advertisements = Advertisement.objects.all()[0:4]


    return render(request, 'NewsApp/home.html', context={
        'all_articles': all_articles,
        'main_article': main_article,
        'r2c1': r2c1_article,
        'r2c2': r2c2_article,
        'r2c3': r2c3_article,
        'r3c1': r3c1_article,
        'r3c2': r3c2_article,
        'r3c3': r3c3_article,
        'r4c1': r4c1_article,
        'r4c2': r4c2_article,
        'r4c3': r4c3_article,
        'r4c4': r4c4_article,
        'r5c1': r5c1_article,
        'r5c2': r5c2_article,
        'r5c3': r5c3_article,
        'r5c4': r5c4_article,
        'advertisements': advertisements
    })





class ArticleCreate( LoginRequiredMixin,CreateView):
    model = NewsArticle
    template_name = 'NewsApp/create.html'
    fields = ['title','content','image','category','importance_level','article_ad']

    def form_valid(self, form):
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = self.request.user
            form_obj.slug = form_obj.title.replace(' ','_')+ str(uuid.uuid4())
            form_obj.save()
        return HttpResponseRedirect(reverse('NewsApp:control'))




class ArticleUpdate(UpdateView, LoginRequiredMixin):
    model = NewsArticle
    template_name = 'NewsApp/update.html'
    fields = ['title','content','image','category','importance_level','article_ad', 'link_ad', 'description_ad']

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('NewsApp:control'))
    

def split_paragraphs(article):
    # Split the text into paragraphs
    paragraphs = article.split('\n')  # Assumes paragraphs are separated by blank lines
    

    if len(paragraphs) > 40:
        a = paragraphs[:20]
        b = paragraphs[20:]
    elif len(paragraphs) > 30 and len(paragraphs) < 40:
        a = paragraphs[:15]
        b = paragraphs[15:]
    elif len(paragraphs) > 20 and len(paragraphs) < 30:
        a = paragraphs[:10]
        b = paragraphs[10:]
    elif len(paragraphs) > 10 and len(paragraphs) < 20:
        a = paragraphs[:8]
        b = paragraphs[8:]
    else:
        a = paragraphs[:5]
        b = paragraphs[5:]

    
    # Join the paragraphs back into strings
    half_content = '\n'.join(a)
    rest_content = '\n'.join(b)
    
    return half_content, rest_content


def details(request,slug):
    article = NewsArticle.objects.get(slug=slug)
    paragraphs = split_paragraphs(article.content)
    half_content, rest_content = paragraphs
    all_articles = NewsArticle.objects.all()[0:5]
    advetisments = Advertisement.objects.all()[0:4]
    title = article.title

    if request.user != article.user:
        article.views += 1
        article.save()

    return render(request, 'NewsApp/details.html', context={'article': article,'all_articles': all_articles, 'title': title, 'advetisments': advetisments,'half_content': half_content, 'rest_content': rest_content})

class DeleteArticle(LoginRequiredMixin,DeleteView):
    model = NewsArticle
    success_url = reverse_lazy('NewsApp:control')
    template_name = 'NewsApp/delete.html'


@login_required
def control_panel(request):
    results = NewsArticle.objects.all()
    search = False
    if request.GET.get('search'):
        search = request.GET.get('search','')
        results = results.filter(title__icontains=search)
    return render(request, 'NewsApp/control.html', context={'results': results, 'search': search})


@login_required
def control_panel_advertisment(request):
    results = Advertisement.objects.all()
    search = False
    if request.GET.get('search'):
        search = request.GET.get('search','')
        results = results.filter(title__icontains=search)
    return render(request, 'NewsApp/control_adv.html', context={'results': results, 'search': search})    


def sorted(request,category):
    articles = NewsArticle.objects.filter(category=category)
    main_article = articles.first()
    first_column = articles[1:3]
    second_column = articles[3:7]
    third_column = articles[7:11]
    row = articles[11:19]
    advertisements = Advertisement.objects.all()[0:4]

    return render(request, 'NewsApp/sorted.html', context={
        'main_article': main_article,
        'first_column': first_column,
        'second_column': second_column,
        'third_column': third_column,
        'row': row,
        'advertisements': advertisements,
    })



def all_articles(request):
    articles = NewsArticle.objects.all()
    advertisements = Advertisement.objects.all()[0:4]
    search = False

    if request.GET.get('search'):
        search = request.GET.get('search','')
        articles = articles.filter(title__icontains=search)

    return render(request, 'NewsApp/all.html', context={'articles': articles, 'advertisements':advertisements, 'search': search})



class Advertising(LoginRequiredMixin, FormView):
    template_name = 'NewsApp/advertising.html'
    form_class = AdvertisementForm
    success_url = reverse_lazy('NewsApp:home')

    def form_valid(self, form):
        form.save()  # Save the form data to create a new Advertisement object
        return super().form_valid(form)
    

def ad_details(request,pk):
    ad = Advertisement.objects.get(pk=pk)
    ad.clicks += 1
    ad.save()
    return render(request, 'NewsApp/ad_details.html', context={'ad': ad})

def article_ad_details(request, slug ):
    article = NewsArticle.objects.get(slug=slug)
    return render(request, 'NewsApp/article_ad_details.html', context={'ad': article})


class Ad_Update(LoginRequiredMixin, UpdateView):
    model = Advertisement
    template_name = 'NewsApp/ad_update.html'
    fields = ['title','content','image','link']
    
    def get_success_url(self):
        return reverse('NewsApp:control_adv')
    

class Ad_Delete(LoginRequiredMixin, DeleteView):
    model = Advertisement
    success_url = reverse_lazy('NewsApp:control_adv')
    template_name = 'NewsApp/ad_delete.html'