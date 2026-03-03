from django.shortcuts import render,redirect,get_object_or_404
from .forms import ContactForm
from .models import ContactMessage

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_success")
    else:
        form=ContactForm()
    return render(request, "contact_us/contact.html", {"form": form})

def contactlist(request):
    contacts = ContactMessage.objects.all()
    return render(request, 'contact_us/contactlist.html', {'contacts': contacts})


def contact_success(request):
    return render(request,'contact_us/contact_success.html')

def contact_detail(request, pk):
    contact = get_object_or_404(ContactMessage, pk=pk)
    return render(request, 'contact_us/contactdetail.html', {'contact': contact})
# Create your views here.
