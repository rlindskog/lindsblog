from django.shortcuts import render
from django.conf import settings

from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_full_name = form.cleaned_data.get('full_name')
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')

        subject = 'Django email'
        from_email = settings.EMAIL_HOST_USER
        to_emails = [from_email]

        contact_message = "%s: %s via %s" % (form_full_name, form_email, form_message)

        send_mail(subject, contact_message, from_email, to_emails, fail_silently=False)

    template = 'contact.html'
    context = {
        'form': form,
    }
    return render(request, template, context)