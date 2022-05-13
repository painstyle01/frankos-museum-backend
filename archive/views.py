from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from  .models import PostArchive
from .serializers import ArchiveSerializer
from api.models import BlogPost
# Create your views here.



def post_save(request, id):
    post = get_object_or_404(BlogPost, id=id)
    archive_post = PostArchive()
    for field in post._meta.fields:
        setattr(archive_post, field.name , getattr(post, field.name))
    archive_post.archived = True
    archive_post.pk = None
    archive_post.save()
    return redirect('archive')
        
@api_view(('GET',))
def get(request):
    archive_posts = PostArchive.objects.all()
    serializer = ArchiveSerializer(archive_posts, many=True)
    return Response(serializer.data)

