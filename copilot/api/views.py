from django.http.response import JsonResponse, HttpResponseServerError
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import datetime
import json

@api_view(['GET'])
def get_current_time(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return JsonResponse({'time': current_time}, status=status.HTTP_200_OK)

@api_view(['GET'])  # Ensure the view only handles GET requests
def hello_world_view(request):
    # Check if the 'hello' parameter is present in the query string
    if 'hello' not in request.GET:
        # Return an HTTP 500 error response if 'hello' is not present
        return HttpResponseServerError("Missing 'hello' query parameter")
    
    # If 'hello' is present, return a JSON response with the message "hello world"
    return JsonResponse({'message': 'hello world'})

@api_view(['GET'])
def get_azure_vms(request):
    """
    Returns a list of Azure VMs from a local JSON file.
    """
    try:
        with open('./data/vms.json', 'r') as file:
            vms = json.load(file)
        return JsonResponse(vms, status=status.HTTP_200_OK, safe= False)
    except FileNotFoundError:
        return JsonResponse(
            {"error": "VMs JSON file not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Error decoding JSON file"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )