from django.shortcuts import render
from django.conf import settings

from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    form = ContactForm(request.POST or None)
    user = request.user
    if form.is_valid():
        message_form = form.cleaned_data.get('message')
        subject_form = form.cleaned_data.get('subject')

        user_email = request.user.email

        from_email = settings.EMAIL_HOST_USER
        to_emails = [settings.EMAIL_HOST_USER]

        subject_string = "Lindsblog Message from %s" % subject_form

        contact_message = "user: %s\nuser_email: %s\nmessage_form: %s" % (user, user_email, message_form)

        send_mail(subject_string, contact_message, from_email, to_emails, fail_silently=False)

    template = 'contact.html'
    context = {
        'form': form,
    }
    return render(request, template, context)