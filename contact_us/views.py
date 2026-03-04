from django.shortcuts import render,redirect,get_object_or_404
from .forms import ContactForm
from .models import ContactMessage
from .forms import Answerform

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
def answer(request):
    contact = ContactMessage
    if request.method == "POST":
            form = Answerform(request.POST, instance=contact)
            if form.is_valid():
                form.save()
    else:
            form=Answerform(instance=contact)
    return render(request, "contact_us/contact.html", {"form": form})

    # Create your views here.
