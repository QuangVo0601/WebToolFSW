from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Input
from .serializers import InputSerializer

# Create your views here.
def index_page(request):
    return HttpResponse("<h1>Server is running correctly</h1>") # Provide initial route 

@csrf_exempt
def input_list(request):
    """
    List all code input, or create a new input obj.
    """
    if request.method == 'GET': # Back End send, Front End request
        inputs = Input.objects.all()
        serializer = InputSerializer(inputs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST': # Back End request, Front End send
        data = JSONParser().parse(request)
        serializer = InputSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def input_detail(request, pk):
    """
    Retrieve, update or delete a code input.
    """
    try:
        input = Input.objects.get(pk=pk)
    except Input.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET': # retrieve data
        serializer = InputSerializer(input)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT': # update data
        data = JSONParser().parse(request)
        serializer = InputSerializer(input, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE': 
        input.delete()
        return HttpResponse(status=204)



