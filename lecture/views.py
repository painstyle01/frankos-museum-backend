from django.core.mail import send_mail
from django.shortcuts import redirect

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import LectureSerializer
from .models import Lecture

# Create your views here.


class LectureView(APIView):

    def get(self, request):
        queryset = Lecture.objects.all()
        serializer = LectureSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        post = Lecture.objects.create(
            name = request.data['name'],
            email = request.data['email'],
            phone = request.data['phone'],
            comment = request.data['comment']
        )
        text = f"Замовив - {request.data['name']}\n адреса -  {request.data['email']}\n телефон - {request.data['phone']}\n коментар - {request.data['comment']}"
        send_mail(
            'Замовлення лекції',
            text,
            'tt0181110@gmail.com',
            ['tt0181110@gmail.com'],
            fail_silently=False
        )
        return redirect('/api')
