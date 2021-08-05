from django.shortcuts import render, redirect, reverse, Http404, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Team
from .forms import AddTeamForm

# Create your views here.


def show_all_teams(request):
    teams = Team.objects.all()
    return render(request, "teams.html", {"teams": teams})


def add_team(request):
    if request.method == 'GET':
        form = AddTeamForm()

        return render(request, 'add_team.html', {
            'form': form,
        })

    if request.method == 'POST':
        form = AddTeamForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, f'Team was successfully added!')

            return redirect(reverse('teams:view_all'))

        # form is not valid!
        return render(request, 'add_team.html', {
            'form': form
        })

    raise Http404('Method not allowed!')


def view_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == "GET":
        context = {"team": team}
        return render(request, "view_team.html", context)

    if request.method == "POST":
        team.delete()
        messages.warning(request, f'Team was successfully deleted!')
        return redirect(reverse('teams:view_all'))


def update_team(request, team_id):
    obj = get_object_or_404(Team, id=team_id)
    form = AddTeamForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Team was successfully updated!')
        return redirect(reverse('teams:view_all'))
    context = {
        'form': form
    }
    return render(request, "update_team.html", context)
