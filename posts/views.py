
from .models import Post
from .serializer import PostSerializer
from rest_framework.generics import  ListCreateAPIView


class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

