from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'leaderboard': '/api/leaderboard/',
        'workouts': '/api/workouts/',
    })

@api_view(['GET', 'POST'])
def users(request):
    user_model = User()
    if request.method == 'GET':
        users = list(user_model.find())
        return Response(users)
    elif request.method == 'POST':
        user_model.insert_one(request.data)
        return Response({'message': 'User created successfully'})

@api_view(['GET', 'POST'])
def teams(request):
    team_model = Team()
    if request.method == 'GET':
        teams = list(team_model.find())
        return Response(teams)
    elif request.method == 'POST':
        team_model.insert_one(request.data)
        return Response({'message': 'Team created successfully'})

@api_view(['GET', 'POST'])
def activities(request):
    activity_model = Activity()
    if request.method == 'GET':
        activities = list(activity_model.find())
        return Response(activities)
    elif request.method == 'POST':
        activity_model.insert_one(request.data)
        return Response({'message': 'Activity created successfully'})

@api_view(['GET', 'POST'])
def leaderboard(request):
    leaderboard_model = Leaderboard()
    if request.method == 'GET':
        leaderboard = list(leaderboard_model.find())
        return Response(leaderboard)
    elif request.method == 'POST':
        leaderboard_model.insert_one(request.data)
        return Response({'message': 'Leaderboard entry created successfully'})

@api_view(['GET', 'POST'])
def workouts(request):
    workout_model = Workout()
    if request.method == 'GET':
        workouts = list(workout_model.find())
        return Response(workouts)
    elif request.method == 'POST':
        workout_model.insert_one(request.data)
        return Response({'message': 'Workout created successfully'})
