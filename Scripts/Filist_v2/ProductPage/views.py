from django.shortcuts import render

# Create your views here.
def productPage(request):
    return render(request, 'ProductPage/productList.html')

def productDetail(request):
    return render(request, 'ProductPage/productDetail.html')

def CartView(request):
    pass

def Json_Response(request):
    pass