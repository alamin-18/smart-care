from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient
from .serializers import   PatientSerializer, UserLoginSerializer,RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
class UserRegisterViewSet(APIView):
    serializer_class = RegistrationSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = f"http://localhost:8000/patient/activate/{uid}/{token}/"
            subject = 'Activate Your Account'
            email_body = render_to_string('activation_email.html', {
                'first_name': user.first_name,
                'activation_link': activation_link,
            })
            email = EmailMultiAlternatives(subject, email_body, to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response({'message': 'User registered successfully. Please check your email to activate your account.'}, status=201)
        return Response(serializer.errors, status=400)
class ActivateAccountView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('http://localhost:3000/login')  # Redirect to login page after activation
        else:
            return Response({'error': 'Activation link is invalid!'}, status=400)
class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({'token': token.key}, status=200)
                else:
                    return Response({'error': 'Account is not activated. Please check your email.'}, status=403)
            else:
                return Response({'error': 'Invalid credentials'}, status=401)
        return Response(serializer.errors, status=400)
class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')