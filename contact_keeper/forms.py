from django.forms import ModelForm, RadioSelect
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
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["placeholder"] = "John Doe"
        self.fields["email"].widget.attrs["placeholder"] = "john@gmail.com"
        self.fields["phone"].widget.attrs["placeholder"] = "(415)555-0938"

    # commit named arg allows save to be delayed as we overwrite
    def save(self, commit=True):
        object = super(ContactForm, self).save(commit=False)
        object.owner = self.owner
        if commit:
            # call the 'real' save method
            object.save()
        return object
