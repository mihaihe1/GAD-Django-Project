from django import forms
from .models import Race


class AddRaceForm(forms.ModelForm):
    class Meta:
        model = Race
        exclude = ['weather']

    def clean(self):
        super(AddRaceForm, self).clean()

        first_place = self.cleaned_data.get('first_place')
        second_place = self.cleaned_data.get('second_place')
        third_place = self.cleaned_data.get('third_place')

        if second_place == first_place:
            self._errors['second_place'] = self.error_class([
                'Driver already picked'])

        if second_place == third_place or first_place == third_place:
            self._errors['third_place'] = self.error_class([
                'Driver already picked'])

        return self.cleaned_data
