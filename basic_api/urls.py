from django.urls import path
from .views import article_list,article_detail,ArticleListView,ArticleDetailView

urlpatterns = [
    path('', article_list),
    path('<int:pk>/', article_detail),
    path('cbv/', ArticleListView.as_view()),
    path('cbv/<int:id>', ArticleDetailView.as_view()),

]
