from django.contrib.auth.models import User

from django.http import JsonResponse

from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import Work, Artist

@api_view(['GET'])

def work_list(request):

    queryset = Work.objects.all()

    artist_name = request.GET.get('artist')

    if artist_name:

        queryset = queryset.filter(artist__name__icontains=artist_name)

    work_type = request.GET.get('work_type')

    if work_type:

        queryset = queryset.filter(link_type=work_type)

    data = [{

        'link': work.link,

        'link_type': work.link_type,

        'artists': [artist.name for artist in work.artist_set.all()]

    } for work in queryset]

    return Response(data)

@api_view(['POST'])

def register(request):

    username = request.data.get('username')

    password = request.data.get('password')

    if not username or not password:

        return Response({'error': 'username and password required'}, status=400)

    user = User.objects.create_user(username=username, password=password)

    return JsonResponse({'user_id': user.id})

