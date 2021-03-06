from django.urls import path
from . import views
from .views import (RecipeDetailView, 
	RecipeListView, 
	RecipeCreateView,
	RecipeUpdateView,
	RecipeDeleteView,
	UserRecipeListView
	)

urlpatterns = [
    path('', RecipeListView.as_view(), name="RecipeBook-Home"),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),  
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe-create'),  
    path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('recipe/<str:username>', UserRecipeListView.as_view(), name='user-recipes'),
]