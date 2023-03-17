from .models import mypost
from django.db.models import Q


def my_search(request):
    search = request.GET.get('search','')
    print(search)
    if search:
        return {'recent_posts':mypost.objects.filter(
                    Q(topic__icontains=search) | Q(author__icontains=search)
                    | Q(content_type__icontains=search) | Q(genre__icontains=search)
                ),}  # Can change numbers for more/fewer posts
    else:
        return {
            'recent_posts':mypost.objects.all()
        }