from django import forms
from my_web.models import contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ('name', 'email', 'message')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # हर field में Bootstrap class जोड़ें
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',  # Bootstrap input styling
                'placeholder': f'Enter your {field}'
            })