from django import forms
from .models import Driver


class AddDriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = []


class FilterDrivers(forms.Form):
    min_podiums = forms.IntegerField(label='Min Nr of Podiums', required=False)
    max_podiums = forms.IntegerField(label='Max Nr of Podiums', required=False)

    def get_drivers(self):
        drivers = Driver.objects.all()
        min_podiums = self.cleaned_data.get('min_podiums')
        max_podiums = self.cleaned_data.get('max_podiums')

        if min_podiums:
            drivers = drivers.filter(podiums__gte=min_podiums)

        if max_podiums:
            drivers = drivers.filter(podiums__lte=max_podiums)

        return drivers
