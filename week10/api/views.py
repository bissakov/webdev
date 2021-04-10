from django.http.response import JsonResponse
from api.models import Product
from api.models import Category

def product_list(request):
    products = Product.objects.all()

    products_json = []
    for product in products:
        products_json.append(product.to_json())

    return JsonResponse(products_json, safe=False)

def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status = 400)

    return JsonResponse(product.to_json())

def category_list(request):
    categories = Category.objects.all()

    categories_json = []
    for category in categories:
        categories_json.append(category.to_json())

    return JsonResponse(categories_json, safe=False)

def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as p:
        return JsonResponse({'message': str(p)}, status = 400)
        
    return JsonResponse(category.to_json())