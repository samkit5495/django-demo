from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'ajaxCall/index.html',{})


def ajaxCall(request):
    data = request.POST['data']
    print(data)
    return JsonResponse({'message':'You entered data:'+data},safe=False)

