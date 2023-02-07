from django import forms
from scraping.models import City, Language


class FindForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name='slug', required=False,
                                  widget=forms.Select(attrs={'class': 'form-control'}), label='Город')
    language = forms.ModelChoiceField(queryset=Language.objects.all(), to_field_name='slug', required=False,
                                      widget=forms.Select(attrs={'class': 'form-control'}), label='Язык программирования')

'''
  <label for="fname">Город:</label><br>
  <input type="text" id="fname" name="city" value=""><br>

  <label for="fname">Язык проги:</label><br>
  <input type="text" name="language" value=""><br>'''