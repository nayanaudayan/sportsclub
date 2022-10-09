from django.shortcuts import render

# Create your views here.
def sports_home(request):
    return render(request,'sports_club_template/home.html')
def sports_about(request):
    return render(request,'sports_club_template/about.html')
def sports_games(request):
    return render(request,'sports_club_template/games.html')
def sports_subscription(request):
    return render(request,'sports_club_template/subscription.html')
def sports_contact(request):
    return render(request,'sports_club_template/contact.html')


   