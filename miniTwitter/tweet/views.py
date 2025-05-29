from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

# read
def tweetList(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweetList.html', {'tweets': tweets})

# create
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

def tweetDelete(request, tweetId):
    tweet = get_object_or_404(Tweet, pk=tweetId, user=request.user)
    
    if(request.method == 'POST'):
        tweet.delete
        return redirect('tweetList')

    return render(request, 'tweetConfirmDelete.html', {'tweet': tweet})
