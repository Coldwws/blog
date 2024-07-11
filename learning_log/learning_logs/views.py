
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from .models import Topic, Entry,Comment
from .forms import TopicForm, EntryForm,CommentForm
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required


class TopicDeleteView(UserPassesTestMixin, DeleteView):
    model = Topic
    success_url = reverse_lazy('learning_logs:topics')

    def test_func(self):
        topic = self.get_object()
        return self.request.user == topic.owner

def index(request):
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    topics = Topic.objects.order_by('date_added')

    context = {'topics': topics}
    return render(request,'learning_logs/topics.html', context )

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, "entries": entries}
    return render(request,"learning_logs/topic.html", context )

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    context = {
        'form':form
    }
    return  render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):

    topic = Topic.objects.get(id = topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id = topic_id)
    context = {
        'topic':topic,
        'form':form
    }

    return render(request, 'learning_logs/new_entry.html', context)



@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry':entry,
               'topic':topic,
               'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)


@login_required
def new_comment(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
           
            new_comment = form.save(commit=False)
            new_comment.entry = entry
            new_comment.save()
            return redirect('learning_logs:topic', topic_id=entry.topic.id)
    else:
       
        form = CommentForm()

    context = {'form': form, 'entry': entry}
    return render(request, 'learning_logs/new_comment.html', context)

@login_required
def delete_comment(request, comment_id):
    
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.user == comment.entry.topic.owner:
        comment.delete()
    else:
        raise Http404("You are not allowed to delete this comment.")

    return redirect('learning_logs:topic', topic_id=comment.entry.topic.id)