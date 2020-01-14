from django import forms
from .models import Posting 

class SearchForm(forms.ModelForm):
    """Used to search for existing job postings.""" 

    keyword_search = forms.CharField(label="Keyword Search", required=False)
    
    class Meta: 
        model = Posting
        fields = ["semester", "position", "school", "percent_time"]


class SubmitPosting(forms.ModelForm):
    """Used to submit new job postings."""
    
    class Meta:
        model = Posting
        exclude = ['content_search']

     
        
        