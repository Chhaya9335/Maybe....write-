from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from .forms import ContributionForm
#from sampleapp import messages

def sample(request):
    return render(request,'index.html')

def creation(request):
    return render(request,'my_creation.html')

def templateview(request):
    return render(request,'index.html')

def review_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # redirect to a thank-you page
    else:
        form = ReviewForm()

    # reviews = Review.objects.filter(approved=True).order_by('-created_at')

    reviews = Review.objects.all().order_by('-created_at')[:4]  # latest first
    return render(request, 'Reviews.html', {'form': form, 'reviews': reviews})


# def message(request):
#messages.success(request, "Thanks for your review! It will be visible after approval.")


def thank_you(request):
    return render(request, 'thank.html')

from django.shortcuts import render, redirect
from .forms import ContributionForm

def contribute_view(request):
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank.html')
    else:
        form = ContributionForm()
    return render(request, 'contribution.html', {'form': form})