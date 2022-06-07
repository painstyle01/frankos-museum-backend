from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect

from rest_framework.views import APIView

from .serializer import LectureSerializer

# Create your views here.


class LectureView(APIView):
    def post(self, request):
        serializer = LectureSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        text = f"Замовив - {request.data['name']}\n Адреса -  {request.data['email']}\n Телефон - {request.data['phone']}\n Коментар - {request.data['comment']}"
        send_mail(
            "Замовлення лекції",
            text,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return redirect("home")
