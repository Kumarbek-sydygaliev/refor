from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LinksForm
from .utils import gen_url
from .models import Links
from django.conf import settings

# Create your views here.

host = settings.ALLOWED_HOSTS[-1]

def test_view(request):
    if request.method == 'POST':
        if not Links.objects.filter(old_link=request.POST['link']):
            Links.objects.create(
                old_link=request.POST['link'])
        new_link = gen_url()
    form = LinksForm()
    links = Links.objects.all().order_by("-id")
    return render(request, "my_app/test.html", context={"form":form, "links":links, "host":host})

def redirect_view(request, new_link):
    result = Links.objects.filter(new_link=new_link).last()
    print(result.old_link)
    return HttpResponseRedirect(result.old_link)
