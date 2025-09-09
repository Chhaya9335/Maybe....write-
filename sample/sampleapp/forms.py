
from django import forms
from .models import Review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating', 'comment']

from django import forms
from .models import Contribution

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'id': 'contribution',
                'placeholder': 'Write your thoughts here...'
            }),
        }
