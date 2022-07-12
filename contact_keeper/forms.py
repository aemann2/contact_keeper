from django.forms import ModelForm, RadioSelect
from django.core.exceptions import ValidationError
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "contact_type"]
        widgets = {
            "contact_type": RadioSelect,
        }

    # overwrite __init__ to set placeholder values
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get("pk")
        if self.pk:
            # popping 'pk' to avoid kwargs error
            kwargs.pop("pk")
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["placeholder"] = "John Doe"
        self.fields["email"].widget.attrs["placeholder"] = "john@gmail.com"
        self.fields["phone"].widget.attrs["placeholder"] = "(415)555-0938"

    # overwriting to check for duplicate entries
    def clean(self):
        data = self.cleaned_data
        pk = self.pk
        owner = self.owner
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        # excluding by pk so we don't get a ValidaionError when editing w/o changes
        duplicate = Contact.objects.filter(
            name=name, email=email, phone=phone, owner=owner
        ).exclude(pk=pk)
        if duplicate:
            raise ValidationError("This contact already exists")

    # commit named arg allows save to be delayed as we overwrite
    def save(self, commit=True):
        object = super(ContactForm, self).save(commit=False)
        object.owner = self.owner
        if commit:
            # call the 'real' save method
            object.save()
        return object
