from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# class-based generic views
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Tag model
from taggit.models import Tag
from django.contrib.auth.models import User
# import models
from .models import Post, Comment #, Like


############## index ##############
def index(request):
    return HttpResponseRedirect(reverse('blog:post_list'))

"""
def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(pk=post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()

    return HttpResponseRedirect(reverse('albums:post_detail', kwargs={'pk': post_id}))
"""


############## views ##############
class PostList(ListView):
    model = Post
    template_name = 'blog/post/post_list.html'
    context_object_name = 'post_list'
    paginate_by = 6

    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Call the base implementation first
        tags = Tag.objects.all() # retrieve all tags
        context['tags'] = tags
        return context
    '''

class PostListByTag(ListView):
    template_name = 'blog/post/post_list.html'
    context_object_name = 'post_list'
    paginate_by = 6

    def get_queryset(self):
        # filter posts by self.kwargs['tag_id']
        tag = get_object_or_404(Tag, pk=self.kwargs['tag_id'])
        return Post.objects.filter(tags__in=[tag]) # tags__in ???

class PostListForSpecificUser(ListView):
    template_name = 'blog/post/post_list.html'
    context_object_name = 'post_list'
    paginate_by = 6

    def get_queryset(self):
        # filter posts for specific user 
        user = get_object_or_404(User, username=self.kwargs['username'])
        return Post.objects.filter(publisher=user)

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # if user is authenticated and owner of post 
        # we add 'is_post_owner' allow user to see 'Update' and 'Delete' buttons
        if self.request.user.is_authenticated and context['post'].publisher == self.request.user:
            context['is_post_owner'] = True
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post/post_form_create.html' 
    fields = ['title', 'description', 'tags', 'image']

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post/post_form_update.html' 
    fields = ['title', 'description', 'tags', 'image']

    def form_valid(self, form):
        # user should be the owner of post
        if form.instance.publisher == self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponse('You are not post woner')

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post/post_confirm_delete.html' 
    success_url = reverse_lazy('blog:post_list')

    # missed how we forbid users who doesn't own the post to 'delete' that post


