from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello,欢迎来到我的页面！</h1>")
