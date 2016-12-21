from rest_framework import serializers

from app.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializing all the Articles
    """

    class Meta:
        model = Article
        fields = ('id', 'title', 'content')
