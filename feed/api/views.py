from rest_framework import generics, permissions
from ..models import Feed, Image, FeedImage, Video, FeedVideo, FeedLike, FeedSave
from .serializer import FeedSerializer, FeedSaveSerializer, ImageSerializer, FeedImageSerializer, VideoSerializer, FeedVideoSerializer, FeedCreateSerializer, FeedLikeSerializer


class FeedCreate(generics.CreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class FeedList(generics.ListAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created_at')

class FeedListFilterByUser(generics.ListAPIView):
    serializer_class = FeedSerializer
    
    def get_queryset(self):
        user = self.request.user
        print("USER",user)
        queryset = Feed.objects.all()
        if user is not None:
            queryset = queryset.filter(user__exact=user)
        return queryset
        


class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class FeedImageList(generics.ListCreateAPIView):
    queryset = FeedImage.objects.all()
    serializer_class = FeedImageSerializer


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class FeedVideoList(generics.ListCreateAPIView):
    queryset = FeedVideo.objects.all()
    serializer_class = FeedVideoSerializer


class FeedLikeAPIView(generics.CreateAPIView):
    queryset = FeedLike.objects.all()
    serializer_class = FeedLikeSerializer
    permission_classes = [permissions.IsAuthenticated]


class FeedSaveAPIView(generics.CreateAPIView):
    queryset = FeedSave.objects.all()
    serializer_class = FeedSaveSerializer
