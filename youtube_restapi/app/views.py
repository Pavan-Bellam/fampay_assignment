from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Videos
from app.serializer import Serializer
from rest_framework.pagination import PageNumberPagination


@api_view(["GET"])
def get_videos(request):
    paginator = PageNumberPagination()
    query_set = Videos.objects.all()
    context = paginator.paginate_queryset(query_set, request)
    serializer = Serializer(context, many=True)

    return paginator.get_paginated_response(serializer.data)
