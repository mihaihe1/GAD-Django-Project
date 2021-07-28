from django.shortcuts import render
# from .models import Team, Pilot
# from .forms import TeamForm
#
# # Create your views here.
#

#
#
# def team_list(request):
#     teams = Team.objects.all()
#     return render(request, "team_list.html", {"teams": teams})
#
#
# def pilot_list(request):
#     pilots = Pilot.objects.all()
#     return render(request, "pilot_list.html", {"pilots": pilots})
#
#
# def team_create_view(request):
#     form = TeamForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#     context = {
#         'form': form
#     }
#     return render(request, "team_create.html", context)
