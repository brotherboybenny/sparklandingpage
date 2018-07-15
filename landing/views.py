from django.shortcuts import render

def post_list(request):
    return render(request, 'landing/post_list.html', {})