from django.urls import path
from .views import article_list,article_detail,ArticleListView,ArticleDetailView,GenericeApiListView,GenericAPIDetailView

urlpatterns = [
    path('', article_list),
    path('<int:pk>/', article_detail),
    path('cbv/', ArticleListView.as_view()),
    path('cbv/<int:id>', ArticleDetailView.as_view()),
    path('gv/',GenericeApiListView.as_view()),
    path('gv/<int:id>',GenericAPIDetailView.as_view()),



]
