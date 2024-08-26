from django.urls import path
from NewsApp import views

app_name = 'NewsApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_post/', views.ArticleCreate.as_view(),name='publish'),
    path('post_edit/', views.ArticleUpdate.as_view(),name='edit'),
    path('details/<slug>/', views.details, name='details'),
    path('ad_details/<pk>/', views.ad_details, name='ad_details'),
    path('article_ad_details/<slug>/', views.article_ad_details, name='article_ad'),
    path('update/<slug>/', views.ArticleUpdate.as_view(),name='update'),
    path('ad_update/<pk>/', views.Ad_Update.as_view(),name='ad_update'),
    path('delete/<slug>/', views.DeleteArticle.as_view(),name='delete'),
    path('ad_delete/<pk>/', views.Ad_Delete.as_view(),name='ad_delete'),
    path('control/', views.control_panel, name='control'),
    path('cont_adv/', views.control_panel_advertisment, name='control_adv'),
    path('sorted/<category>/', views.sorted, name='sorted'),
    path('all/', views.all_articles, name='all'),
    path('advertising', views.Advertising.as_view(), name='advertising'),
]