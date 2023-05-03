from django.shortcuts import render, redirect
from .models import Dining, Review, Menu
from .forms import DiningForm, ReviewForm, MenuForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.


def index(request):
    dinings = Dining.objects.order_by("-pk")
    context = {
        'dinings': dinings,
    }
    return render(request, 'dinings/index.html', context)

def showmap(request):
    return render(request, 'dinings/showmap.html')


def detail(request, pk):
    dining = Dining.objects.get(pk=pk)
    reviews = dining.review_set.all()
    menu_form = MenuForm(request.POST)
    menus = dining.menu_set.all()

    sum = 0
    avg = 0

    # zero division error 때문에 조건문 추가
    if reviews:
        for review in reviews:
            sum += review.rating
        # 총 평점을 나타내기 위해 avg 변수에 평균 할당
        avg = round(sum / len(reviews), 1)
    context = {
        'dining': dining,
        'reviews': reviews,
        'avg': avg,
        'menus': menus,
        'menu_form': menu_form,
    }
    return render(request, 'dinings/detail.html', context)


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
    return render(request, 'dinings/dining_create.html', context)


@login_required
def review_create(request, dining_pk):
    dining = Dining.objects.get(pk=dining_pk)

    # 리뷰 작성
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            print(review_form.cleaned_data)
            review = review_form.save(commit=False)
            review.user = request.user
            review.dining = dining
            review.save()
            review_form.save_m2m()
            return redirect('dinings:detail', dining.pk)
    # 리뷰 작성 페이지
    else:
        review_form = ReviewForm()
    context = {
        'review_form': review_form,
        'dining': dining,
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
            review_form = ReviewForm(
                request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                review_form.save()
                return redirect('dinings:detail', dining_pk)

        else:
            review_form = ReviewForm(instance=review)
    else:
        return redirect('dinings:detail', dining_pk)
    context = {
        'review_form': review_form,
        'dining_pk': dining_pk,
        'review_pk': review_pk,
    }
    return render(request, 'dinings/review_update.html', context)


@login_required
def dining_update(request, dining_pk):
    dining = Dining.objects.get(pk=dining_pk)
    if request.method == 'POST':
        form = DiningForm(request.POST, instance=dining)
        if form.is_valid():
            form.save()
            return redirect('dining:detail', dining_pk)
    else:
        form = DiningForm(instance=dining)
    context = {
        'form': form,
        'dining': dining
    }
    return render(request, 'dinings/dining_update.html', context)


@login_required
def dining_delete(requset, dining_pk):
    dining = Dining.objects.get(pk=dining_pk)
    dining.delete()
    return redirect('dinings:index')


# def search(request):
#     query = None
#     search_list = None

#     if 'q' in request.GET:
#         query = request.GET.get('q')
#         search_list = Dining.objects.filter(
#             Q(title__icontains=query) |
#             Q(tags__name__icontains=query)
#         ).distinct()
#     context = {
#         'query': query,
#         'search_list': search_list,
#     }
#     return render(request, 'dinings/search.html', context)


def search(request):
    query = request.GET.get('query')
    dinings = Dining.objects.filter(title__icontains=query)
    context = {'dinings': dinings}
    return render(request, 'dinings/search.html', context)


@login_required
def menu_create(request, dining_pk):
    dining = Dining.objects.get(pk=dining_pk)
    menu_form = MenuForm(request.POST)

    if menu_form.is_valid():
        menu = menu_form.save(commit=False)
        menu.dining = dining
        menu.save()
        return redirect('dinings:detail', dining_pk)

    context = {
        'dining': dining,
        'menu_form': menu_form,
    }
    return render(request, 'dinings/detail.html', context)


@login_required
def likes(reqeust, dining_pk):
    dining = Dining.objects.get(pk=dining_pk)

    if dining.like_users.filter(pk=reqeust.user.pk).exists():
        dining.like_users.remove(reqeust.user)
    else:
        dining.like_users.add(reqeust.user)
    return redirect('dinings:detail', dining_pk)


