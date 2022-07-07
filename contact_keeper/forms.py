from django.forms import ModelForm, RadioSelect
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "contact_type"]
        widgets = {"contact_type": RadioSelect}

    # commit named arg allows save to be delayed as we overwrite
    def save(self, commit=True):
        object = super(ContactForm, self).save(commit=False)
        object.owner = self.owner
        if commit:
            # call the 'real' save method
            object.save()
        return object
