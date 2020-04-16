from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post,Comment
from django.contrib.auth.models import User


def home(request):
    return render(request,'blog/home.html',{'posts':Post.objects.all(),'title':'Homepage'})
    
def about(request):
    return render(request,'blog/about.html',{'title':'AboutPage'})


class PostDetailView(DetailView):
    model=Post
    context_object_name='post'
   
class PostListView(ListView):
    model=Post
    template_name="blog/home.html"
    ordering=['-date_posted']
    context_object_name="posts"
    paginate_by=5
class CommentListView(ListView):
    model=Post
    template_name="blog/post_detail.html"
    context_object_name="post"
    
    
    
   
class UserPostListView(ListView):
    model=Post
    template_name="blog/user_posts.html"
    
    context_object_name="posts"
    paginate_by=5
    
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by('-date_posted')
        
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class CommentCreateView(LoginRequiredMixin,CreateView):
            model=Comment
            fields=['content',]
            
            def form_valid(self,form):
                id=get_object_or_404(Post,id=self.kwargs.get("pk"))
                form.instance.post_author=id
                form.instance.author=self.request.user
                return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url="/blog/"
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False
