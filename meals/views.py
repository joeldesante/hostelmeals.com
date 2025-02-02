from django.template import loader
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Recipe

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {
        "recipes": Recipe.objects.all().order_by('-updated_at').values()
    }
    return HttpResponse(template.render(context, request))

def recipe(request, slug):

    recipe = get_object_or_404(Recipe, slug=slug)
    
    template = loader.get_template('recipe.html')
    context = {
        "recipe": recipe
    }
    return HttpResponse(template.render(context, request))

def add_recipe(request):
    template = loader.get_template('add_recipe.html')
    context = {}
    return HttpResponse(template.render(context, request))