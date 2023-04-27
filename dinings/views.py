from django.shortcuts import render, redirect
from .models import Dining, Review
from .forms import DiningForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    dinings = Dining.objects.all()
    context = {
        'dinings':dinings,
    }
    return render(request, 'dinings/index.html',context)

# @login_required
def dining_create(request):
    if request.method == 'POST':
        form = DiningForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dinings:index')
    else:
        form = DiningForm()
    context = {
        'form': form,
    }
    return render(request, 'dinings/create.html', context)

def dining_detail(request, dining_pk):
    dining = Dining.objects.get(pk=dining_pk)
    review_form = ReviewForm()
    reviews = dining.reviews.all()
    context = {
        'dining': dining,
        'review_form': review_form,
        'reviews':reviews,
    }
    return render(request, 'dinings/details.html', context)

# @login_required
def dining_update(request, dining_pk):
    dining = Dining.objects.get(pk=dining_pk)
    if request.method == "POST":
        form = DiningForm(request.POST, instance=dining)
        if form.is_valid():
            form.save()
            return redirect('dinings:dining_detail', dining_pk)
    else:
        form = DiningForm(instance=dining)
    context = {
        'dining': dining,
        'form':form,
    }
    return render(request, 'dinings/update.html',context)

# @login_required
def dining_delete(requset, dining_pk):
    dining = Dining.objects.get(pk=dining_pk)
    dining.delete()
    return redirect('dinings:index')

@login_required
def review_create(request, dining_pk):
    dining = Dining.objects.get(pk=dining_pk)
    
    # 리뷰 작성
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.dining = dining
            review.save()
            return redirect('dinings:detail.html', dining.pk)
    # 리뷰 작성 페이지
    else:
        review_form = ReviewForm()
    context = {
        'review_form': review_form,
    }
    return render(request, 'dinings/review_create.html', context)


@login_required
def review_detail(request, dining_pk, review_pk):
    review = Review.objects.get(pk=review_pk)

    # 리뷰 공감
    if request.method == 'POST':
        dining = Dining.objects.get(pk=dining_pk)
        if dining.like_users.filter(pk=request.user.pk).exists():
            dining.like_users.remove(request.user)
        else:
            dining.like_users.add(request.user)
        return redirect('dinings:detail', dining.pk)
    
    # 리뷰 삭제
    elif request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
        return redirect('dinings:index')
    

@login_required
def review_update(request, dining_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    
    if request.user == review.user:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                review_form.save()
                return redirect('dinings:detail', dining_pk)

        else:
            review_form = ReviewForm(instance=review)
    else:
        return redirect('dinings:detail', dining_pk)
    context = {
        'review_form': review_form,
    }
    return render(request, 'dinings/review_update.html', context)