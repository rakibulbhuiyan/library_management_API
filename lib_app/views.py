from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.utils import timezone
from django.db import transaction
from .models import User, Author, Category, Book, Borrow
from .serializers import ( RegisterSerializer, UserSerializer, AuthorSerializer,
                           CategorySerializer, BookSerializer, BorrowSerializer )

# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Admins can manage (books, authors, and categories), so permissions are make here...
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [permissions.IsAdminUser()]    #    here permission for admin user
        return [permissions.AllowAny()]           #    here permission for any user


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAdminUser]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

# ----------------  Permission End ---------------//

#-----------------start borrow instr----------------//

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def borrow_book(request):
    user = request.user
    book_id = request.data.get('book_id')
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=404)

    if book.available_copies <= 0:
        return Response({'error': 'No copies available'}, status=400)
    
    # Users have a borrowing limit (max 3 books at once)
    active_borrows = Borrow.objects.filter(user=user, return_date__isnull=True).count()
    if active_borrows >=3:
         return Response({'error': 'Borrowing limit reached'}, status=400)
    
    # Books have multiple copies, only available copies can be borrowed
    with transaction.atomic():
        book.available_copies -=1
        book.save()
        borrow = Borrow.objects.create(user=user, book=book)

    return Response({'message': 'Book borrowed successfully', 'due_date': borrow.due_date})

    
    
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def return_book(request):
    borrow_id = request.data.get('borrow_id')
    try:
        borrow = Borrow.objects.get(id=borrow_id, user=request.user)
    except Borrow.DoesNotExist:
        return Response({'error': 'Borrow record not found'}, status=404)
    
    if borrow.return_date:
        return Response({'error': 'Book already returned'}, status=400)
    
    with transaction.atomic():
        now = timezone.now()
        borrow.return_date = now
        borrow.save()

        book = borrow.book
        book.available_copies += 1
        book.save()

        # Check for late return
        if now > borrow.due_date:
            late_days = (now.date() - borrow.due_date.date()).days
            request.user.penalty_points += late_days
            request.user.save() 

    return Response({'message': 'Book returned successfully'})


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_penalty_view(request, id):
    if request.user.id != id and not request.user.is_staff:
        return Response({'error': 'Permission denied'}, status=403)

    user = User.objects.get(id=id)
    return Response({'penalty_points': user.penalty_points})