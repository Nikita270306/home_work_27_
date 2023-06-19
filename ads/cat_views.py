import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Categories


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()

        response = []
        for category in categories:
            response.append({
                "name": category.name
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        category_data = json.loads(request.body)

        category = Categories.objects.create(
            name=category_data['name']
        )

        return JsonResponse({
            "name": category.name
        })


class CategoryDetailView(DetailView):
    model = Categories
    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            "name": category.name
        })
