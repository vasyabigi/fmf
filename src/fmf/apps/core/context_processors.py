from stories.models import Category

def categories(request):
    return {'categories': Category.objects.filter(is_active=True)}
