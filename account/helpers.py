from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
def email_template(user, amount, subject, template):
  message = render_to_string(template, {
      'user' : user,
      'amount' : amount,
  })
  send_email = EmailMultiAlternatives(subject, '', to=[user.email])
  send_email.attach_alternative(message, "text/html")
  send_email.send()