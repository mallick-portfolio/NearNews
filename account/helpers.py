from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
def email_template(email, data, subject, template):
  message = render_to_string(template, {
      'data' : data,
  })
  send_email = EmailMultiAlternatives(subject, '', to=[email])
  send_email.attach_alternative(message, "text/html")
  send_email.send()