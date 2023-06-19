import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import ADS, Categories


@method_decorator(csrf_exempt, name="dispatch")
class TestView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AllAdsView(View):
    def get(self, request):
        adses = ADS.objects.all()

        response = []
        for ads in adses:
            response.append({
                "name": ads.name,
                "author": ads.author,
                "price": ads.price,
                "description": ads.description,
                "address": ads.address,
                "is_published": ads.is_published
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        ads_data = json.loads(request.body)

        ads = ADS.objects.create(
            name=ads_data['name'],
            author=ads_data['author'],
            price=ads_data['price'],
            description=ads_data['description'],
            address=ads_data['address'],
            is_published=ads_data['is_published']
        )

        return JsonResponse({
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        })


class AdsDetailView(DetailView):
    model = ADS
    def get(self, request, *args, **kwargs):
        ads = self.get_object()

        return JsonResponse({
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        })
