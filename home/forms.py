from django import forms

from .models import Booking

class Dateinput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={
            'booking_date': Dateinput(),
            
        }

        labels={
            'p_name':'Patient Name:',
            'p_phone': 'Patient Phone Number:',
            'p_email':'Patient Email:',
            'doct_name':'Doctor Name:',
            'booking_date':'Booking Date:'
        }


doct_img =forms.ImageField(
    label="Doctors Image",
    widget=forms.ClearableFileInput(attrs={
        'class':'form-control'
    })
)