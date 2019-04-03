from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def testClientSSO(request):
	json_data = {'name': 'post', 'id': 0}
	return JsonResponse(json_data)