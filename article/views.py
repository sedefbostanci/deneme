from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from article.models import Article
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from rest_framework.parsers import JSONParser
from .serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

class ArticleAPIView(APIView):

    def get(self,request):
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)

        return Response(serializer.data)

    def post(self,request):

        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class NotDetail(DetailView):

    model = Article
    fields = ['content']
    template_name='details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class NotDelete(DeleteView):

    model = Article
    success_message = "Note deleted successfully"
    template_name ="not_delete.html"
    success_url ="/articles/view_notes"

class NotCreate(SuccessMessageMixin,CreateView):
    model = Article
    fields = ['title','content']
    template_name='add_notes.html'

    success_message = "Note created successfully"
    def form_valid(self, form):
        form.instance.author = self.request.user

        return super(NotCreate, self).form_valid(form)

class NotUpdate(UpdateView):
    model = Article
    fields = ['title','content']
    template_name = 'update_note.html'

class ArticleListView(ListView):

    model = Article
    context_object_name = 'my_notes'
    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

# Create your views here.
def index(request):
    return render(request,"index.html")

def add_notes(request):
    return render(request,"add_notes.html")

def article_api(request):
    if request.method=='GET':
        articles=Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method=='POST':
        data=JSONParser.parse(request)
        serializer=ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt

def article_detail(request,pk):
    try:
        article=Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method=='GET':
        serializer=ArticleSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method=='PUT':
        data=JSONParser.parse(request)
        serializer=ArticleSerializer(article,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)

    if request.method=='DELETE':
        article.delete()
        return HttpResponse(status=204)
