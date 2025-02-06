from django.template import loader
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Recipe
import json

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

    if not request.user.is_authenticated:
        return HttpResponse("Please log in.")

    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)

        recipe = Recipe(
            slug = data['slug'],
            article_name = data['full_name'],
            short_name = data['short_name'],
            description = data['description'],
            article = data['story'],
            ingredients = data['ingredients'],
            procedure = data['steps'],
        )
        recipe.save()

        return HttpResponse("OK")

    template = loader.get_template('add_recipe.html')
    context = {}
    return HttpResponse(template.render(context, request))