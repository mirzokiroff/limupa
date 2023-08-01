from django.forms import Form, CharField, EmailField


class ContactForm(Form):
    name = CharField(max_length=255)
    email = EmailField(max_length=255)
    subject = CharField(max_length=255)
    text = CharField()