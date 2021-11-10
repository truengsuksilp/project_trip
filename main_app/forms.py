from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    # Call method on form itself
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        if len(first_name) < 3:
            self.add_error('first_name', "too short")
            
            # ValidationError Method doesn't work
            # raise forms.ValidationError({'first_name', 'Validation: Too short'})

            # Added to HTML 
            #    {% for error in non_field_errors %}
            #      <p style="color: purple">{{ error }}</p>
            #    {% endfor %}

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2', )
    
    