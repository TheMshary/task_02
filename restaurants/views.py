from django.shortcuts import render

# Create your views here.
def nothing(request):
	return render(request, "nothing.html", {"msg": "Hello World!"})