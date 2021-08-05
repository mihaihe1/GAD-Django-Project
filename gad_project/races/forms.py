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


class FilterRaces(forms.Form):
    starting_date = forms.DateTimeField(label='Starting Date', required=False)
    ending_date = forms.DateTimeField(label='Ending Date', required=False)
    sold_out = forms.BooleanField(label='Sold Out', required=False)

    def get_races(self):
        races = Race.objects.all()

        sold_out = self.cleaned_data.get('sold_out')

        if sold_out:
            races = races.filter(sold_out=True)

        starting_date = self.cleaned_data.get('starting_date')
        ending_date = self.cleaned_data.get('ending_date')

        if starting_date:
            races = races.filter(date__gte=starting_date)

        if ending_date:
            races = races.filter(date__lte=ending_date)

        return races
