from rest_framework import viewsets
from .models import Author, Editor, Book, Category, Copy, Loan, Comment, Evaluation
from .serializers import AuthorSerializer, EditorSerializer, BookSerializer, CategorySerializer, CopySerializer, LoanSerializer, CommentSerializer, EvaluationSerializer
from .pagination import StandardResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .permissions import IsCopyAdmin, IsCopyReadOnlyUser
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.views import TokenObtainPairView

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'birthdate', 'death','nationality']
    ordering_fields = ['name', 'birthdate', 'death', 'nationality']
    ordering = ['name']

class EditorViewSet(viewsets.ModelViewSet):
    queryset = Editor.objects.all()
    serializer_class = EditorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_date']
    ordering_fields = ['title', 'publication_date', 'author']
    ordering = ['title']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CopyViewSet(viewsets.ModelViewSet):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsCopyAdmin()]
        return [IsCopyReadOnlyUser()]

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    @method_decorator(ratelimit(key='ip', rate='5/5s', method='POST', block=True))
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)