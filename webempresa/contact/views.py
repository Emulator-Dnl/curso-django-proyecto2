from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # TODO: Arreglar el envío de correos, siempre manda a fail
            # enviamos el correo y redireccionamos
            email = EmailMessage(
                "Cafe chido, nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["dan18642@hotmail.com"],
                reply_to=[email],
            )
            try:
                email.send()

                #Algo salió bien, redirecionamos a OK
                return redirect(reverse('contact')+'?ok')
            except:
                #Algo salió mal, redirecionamos a FAIL
                return redirect(reverse('contact')+'?fail')

            


    return render(request, "contact/contact.html", {'form':contact_form})