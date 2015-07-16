from Onboard.utils import CallOnce
from django.shortcuts import render
from .forms import SignUpForm,ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    title = 'Bem Vindo'

    if request.user.is_authenticated():
       title = 'Condominio Edificio Cleucy, Bem vindo: %s' %(request.user)

    form = SignUpForm(request.POST or None)

    context={
        "title": title,
        "form" : form,
    }

    if form.is_valid():
        # form.save()
       # print(request.POST['email'])
        instance = form.save(commit=False)

        Nome = form.cleaned_data.get("Nome")
        if not Nome:
            Nome = "New Nome"
        instance.Nome = Nome
        instance.save()
        context={
            "title": "Obrigado!"

        }

    return render(request,'home.html',context)


def contact(request):

    form = ContactForm(request.POST or None)

    if form.is_valid():
        # for key, value  in form.cleaned_data.items():
        #     print(key,value)

        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_Nome = form.cleaned_data.get("Nome")
        print('Teste',form_email,form_message,form_Nome)

        subject = "Site Contact Form"
        from_email = settings.EMAIL_HOST_USER
        to_email = ['felipepagliuco@gmail.com']
        contact_message = "%s : %s via %s"%(
            form_Nome,
            form_message,
            form_email
        )

        send_mail( subject,
                   contact_message,
                   from_email,
                   to_email,
                   fail_silently=False)

        # send_mail(subject, 'Here is the message.',from_email, ['felipepagliuco@gmail.com'], fail_silently=False)
        # send_mail('Subject here', 'Here is the message.', 'from@example.com',['to@example.com'], fail_silently=False)
    context = {
        "form": form
    }
    return render(request,'forms.html',context)

