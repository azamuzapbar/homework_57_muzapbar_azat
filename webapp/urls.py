from django.contrib import admin
from django.urls import path
from webapp.views import IndexView
from webapp.articles import (
    ArticleView,
    ArticleUpdateView,
    delete_view,
    confirm_delete,
    add_view
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('articles/add/', add_view, name='article_add'),
    path('articles/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', delete_view, name='article_delete'),
    path('articles/<int:pk>/confirm-delete/', confirm_delete, name='confirm_delete'),
    path('articles/<int:pk>', ArticleView.as_view(), name='article_detail')
]

