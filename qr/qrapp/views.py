from pickle import GET
from django.shortcuts import render
from .forms import UrlForm
import qrcode
import PIL
# Create your views here.
def home(request):
    form = UrlForm()
    return render(request,"qrapp/home.html",{"form": form})

def index(request):

    form = UrlForm(request.GET)
    if form.is_valid():
        input_data = form.cleaned_data["url"]
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save("qr.png")
    return render(request,"qrapp/index.html")
    
