from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, BookViewSet, AuthorViewSet, CategoryViewSet,
    borrow_book, return_book, user_penalty_view
)

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('borrow/', borrow_book),
    path('return/', return_book),
    path('users/<int:id>/penalties/', user_penalty_view),
    path('', include(router.urls)),
]
