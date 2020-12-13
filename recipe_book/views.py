from django.shortcuts import render
from .models import Recipe
from django.views.generic import (
	DetailView, 
	ListView, 
	CreateView,
	UpdateView,
	DeleteView
	)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class RecipeDetailView(DetailView):
	model = Recipe


class RecipeListView(ListView):
	model = Recipe
	template_name = 'recipe_book/home.html'
	ordering = ['-date_created', '-date_updated']

class RecipeCreateView(LoginRequiredMixin, CreateView):
	model = Recipe
	fields = ['recipe_name', 'description', 'instructions']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Recipe
	success_url = '/'

	def test_func(self):
		recipe = self.get_object()
		return self.request.user == recipe.author

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Recipe
	fields = ['recipe_name', 'description', 'instructions']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		recipe = self.get_object()
		return self.request.user == recipe.author



