from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from .permissions import ReviewerOrReadOnly
from rest_framework import status, generics
from .models import StreamPlatform, WatchList, Review
from .serializers import StreamPlatformSerializer,WatchListSerializer, ReviewSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class WatchListView(APIView):
    authentication_classes = [JWTAuthentication]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]  # Anyone can access GET requests
        elif self.request.method == 'POST':
            return [IsAuthenticated()]  # Only authenticated users can make POST requests
        return super().get_permissions()
    
    def get(self, request):
        watchlist=WatchList.objects.all()
        serializer=WatchListSerializer(watchlist, many=True)
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)            

class WatchListDetailView(APIView):
    def get(self, request, pk):
        try:
            watchlist=WatchList.objects.get(pk=pk) 
            serializer=WatchListSerializer(watchlist)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except WatchList.DoesNotExist as e:
            return Response({"error":str(e)},status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk):
        try:
            watchlist=WatchList.objects.get(pk=pk) 
            serializer=WatchListSerializer(watchlist,data=request.data)
            if serializer.is_valid():
                serializer.save()       
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except WatchList.DoesNotExist as e:
            return Response({"error":str(e)},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        try:
            watchlist=WatchList.objects.get(pk=pk)    
            watchlist.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except WatchList.DoesNotExist as e:
            return Response({"error":str(e)},status=status.HTTP_404_NOT_FOUND)        

class StreamListView(APIView):
    def get(self, request):
        stream=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(stream, many=True)
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    


class StreamDetailView(APIView):
    def get(self, request, pk):
        try:
            stream = StreamPlatform.objects.get(pk=pk)
            serializer=StreamPlatformSerializer(stream)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except StreamPlatform.DoesNotExist as e:
            return Response({"error":str(e)},status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk):
        try:
            stream=StreamPlatform.objects.get(pk=pk) 
            serializer=WatchListSerializer(stream,data=request.data)
            if serializer.is_valid():
                serializer.save()       
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except StreamPlatform.DoesNotExist as e:
            return Response({"error":str(e)},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        try:
            stream=StreamPlatform.objects.get(pk=pk)    
            stream.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except StreamPlatform.DoesNotExist as e:
            return Response({"error":str(e)},status=status.HTTP_404_NOT_FOUND)        


class ReviewListView(generics.ListAPIView):
    serializer_class=ReviewSerializer
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewCreate(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        watchlist=WatchList.objects.get(pk=pk)
        user=self.request.user
        if Review.objects.filter(watchlist=watchlist, reviewed_user=user).exists():
            raise ValidationError('You already made a review for this movie')
        
        if watchlist.number_ratting == 0:
            watchlist.avg_ratting = serializer.validated_data['rating']
        
        watchlist.avg_ratting = (watchlist.avg_ratting+serializer.validated_data['rating'])/2
        watchlist.number_ratting = watchlist.number_ratting + 1
        watchlist.save()
        serializer.save(watchlist=watchlist, reviewed_user=user)
    

# class ReviewListView(APIView):
#     def get(self, request,**kwargs):
#         watch = WatchList.objects.get(pk=kwargs['pk'])
#         reviews = Review.objects.filter(watchlist=watch)
#         serializer= ReviewSerializer(reviews,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def post(self, request, **kwargs):
#         try:
#             reviewed_user=self.request.user
#             watchlist = WatchList.objects.get(pk=kwargs['pk'])    
#             if watchlist:
#                 serializer = ReviewSerializer(data=request.data)   
#                 if serializer.is_valid():
#                     serializer.save(watchlist=watchlist,reviewed_user=reviewed_user)
#                     return Response(serializer.data, status=status.HTTP_201_CREATED)
#                 else:
#                     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except WatchList.DoesNotExist as e:
#             return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)            

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[ReviewerOrReadOnly]

    
# class ReviewDetailView(APIView):
#     def get(self, request, pk):
#         try:
#             review = Review.objects.get(pk=pk)
#             serializer = ReviewSerializer(review)
#             return Response(serializer.data, status=status.HTTP_200_OK)        
#         except Review.DoesNotExist as e:
#             return Response({'error':str(e)},status=status.HTTP_404_NOT_FOUND)
    
#     def patch(self, request, pk):
#         try:
#             review = Review.objects.get(pk=pk)
#             serializer = ReviewSerializer(review, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)        
#         except Review.DoesNotExist as e:
#             return Response({'error':str(e)},status=status.HTTP_404_NOT_FOUND)
    
#     def delete(self, request, pk):
#         try:
#             review = Review.objects.get(pk=pk)
#             review.delete()
#             return Response({'data':[]},status=status.HTTP_204_NO_CONTENT)        
#         except Review.DoesNotExist as e:
#             return Response({'error':str(e)},status=status.HTTP_404_NOT_FOUND)