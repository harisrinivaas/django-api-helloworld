from app.models import Article
from app.serializers import ArticleSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get_articles(request):
    if request.method == 'GET':
        posts = Article.objects.all()
        serializer = ArticleSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_article(request, pk):
    try:
        post = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(post)
        return Response(serializer.data)


@api_view(['POST'])
def save_article(request):
    print("posting#")
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_article(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
