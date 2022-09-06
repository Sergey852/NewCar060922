from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .forms import GeeksForm
from .models import *
# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        context = GeeksForm()
        banner = Banner.objects.all()
        onecolumn = HomeOnecolumn.objects.all()
        twocolumns = HomeTwocolumns.objects.all()
        threecolumns = HomeThreecolumns.objects.all()
        social = Social.objects.all()
        slider = HomeSlider.objects.all()
        return render(request, self.template_name, {'slider':slider, "banner":banner, "context":context, "social":social, "onecolumn":onecolumn, "twocolumns":twocolumns, "threecolumns":threecolumns})

class AboutListView(ListView):
    template_name = 'about.html'

    def get(self, request):
        banner = Banner.objects.all()
        slider = HomeSlider.objects.all()
        social = Social.objects.all()
        aboutus = Aboutus.objects.all()
        aboutus2 = Aboutus2.objects.all()
        return render(request, self.template_name, {"aboutus":aboutus, "aboutus2":aboutus2,"social":social,'slider':slider, "banner":banner})

class AboutdetailListView(DetailView):
    template_name = 'about_details.html'

    def get(self, request, id):
        banner = Banner.objects.all()
        slider = HomeSlider.objects.all()
        social = Social.objects.all()
        aboutusdetail = Aboutus.objects.get(pk=id)
        return render(request, self.template_name, {"aboutusdetail":aboutusdetail,  "social":social,'slider':slider, "banner":banner})

class Aboutdetail2ListView(DetailView):
    template_name = 'about_details2.html'

    def get(self, request, id):
        banner = Banner.objects.all()
        slider = HomeSlider.objects.all()
        social = Social.objects.all()
        aboutusdetail2 = Aboutus2.objects.get(pk=id)
        return render(request, self.template_name, { "aboutusdetail2":aboutusdetail2, "social":social,'slider':slider, "banner":banner})

class ContactListView(ListView):
    template_name = 'contact.html'

    def get(self, request):
        banner = Banner.objects.all()
        slider = HomeSlider.objects.all()
        social = Social.objects.all()
        return render(request, self.template_name, { "social":social,'slider':slider, "banner":banner})


class GalleryListView(ListView):
    template_name = 'gallery.html'

    def get(self, request):
        banner = Banner.objects.all()
        slider = HomeSlider.objects.all()
        social = Social.objects.all()
        photo = Galleryphoto.objects.all()
        galcount = Galleryphoto.objects.all().count()
        return render(request, self.template_name, {"galcount":galcount, "photo":photo, "social":social,'slider':slider, "banner":banner})

class GalleryphotoDetailView(DetailView):
    template_name = 'Gallery_view_more.html'

    def get(self, request,id):
        banner = Banner.objects.all()
        slider = HomeSlider.objects.all()
        social = Social.objects.all()
        photoabout = Galleryphoto.objects.get(pk=id)
        
        return render(request, self.template_name, {"photoabout":photoabout,  "social":social,'slider':slider, "banner":banner})

class ProductsListView(ListView):
    template_name = 'products.html'

    def get(self, request):
        banner = Banner.objects.all()
        callus = Callus.objects.all()
        slider = HomeSlider.objects.all()
        category = Newcategory.objects.all()
        social = Social.objects.all()
        prodcount = Newcategory.objects.all().count()
        carcount = Car.objects.all().count()


        return render(request, self.template_name, {"carcount":carcount, "prodcount":prodcount, "social":social,'category':category, 'slider':slider, "banner":banner, "callus":callus })

class CarCategListView(ListView):
    template_name = 'cars.html'

    def get(self, request, id):
        cars = Newcategory.objects.filter(pk=id)
        social = Social.objects.all()
        return render(request, self.template_name, { "social":social,'cars':cars  })

class ServicesListView(ListView):
    template_name = 'services.html'

    def get(self, request):
        banner = Banner.objects.all()
        slider = HomeSlider.objects.all()
        social = Social.objects.all()
        custser = Customer_services.objects.all()
        secondcolumn = Services_second_column.objects.all()
        return render(request, self.template_name, {"secondcolumn":secondcolumn, "custser":custser,"social":social,'slider':slider, "banner":banner})