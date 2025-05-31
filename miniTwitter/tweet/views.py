from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, RegisterForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

# read
def tweetList(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweetList.html', {'tweets': tweets})

# create
@login_required
def tweetCreate(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES) # request.FILES if you are accepting files either
        # in django you get bydefault an user when you are using form
        if(form.is_valid):
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweetList')
    else:
        form = TweetForm() # i.e user has given empty form
    
    return render(request, 'tweetForm.html', {'form': form}) # render(request, whereToRender, dataSend)

# edit
@login_required
def tweetEdit(request, tweetId):
    tweet = get_object_or_404(Tweet, pk=tweetId, user=request.user) # to only get to edit your own tweet
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if(form.is_valid):
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweetList')
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweetForm.html', {'form': form})

@login_required
def tweetDelete(request, tweetId):
    tweet = get_object_or_404(Tweet, pk=tweetId, user=request.user)
    
    if(request.method == 'POST'):
        tweet.delete()
        return redirect('tweetList')

    return render(request, 'tweetConfirmDelete.html', {'tweet': tweet})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweetList')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


