from django.shortcuts import render, reverse, redirect
from django.db import connection
from django.contrib.postgres.search import SearchVector
from .models import Posting
from .forms import SearchForm, SubmitPosting

def index(request):
    """The home page for ASE Database."""
    
    if request.method != "POST":
        #No data submitted; render home page 
        form = SearchForm()
        
        #Display a blank or invalid form 
        context = {
            "form": form,
        }
        return render(request, "ase_site/index.html", context)
        

def results(request):
    """Results page for search queries."""
    
    semester_query = request.GET.get("semester")
    position_query = request.GET.get("position")
    school_query = request.GET.get("school")
    percent_query = request.GET.get("percent_time")
    
    keywords = request.GET.get("keyword_search")
    
    if not keywords == "":
        print("a")
        qs = Posting.objects.filter(content_search=keywords).filter(semester__icontains=semester_query, position__icontains=position_query,
            school__icontains=school_query).order_by("position")
        
    elif percent_query == "":
        print("b")
        qs = Posting.objects.filter(semester__icontains=semester_query, position__icontains=position_query,
            school__icontains=school_query).order_by("position")

    else:
        print("c")
        qs = Posting.objects.filter(semester__icontains=semester_query, position__icontains=position_query,
        school__icontains=school_query, percent_time__icontains=percent_query).order_by("position")

    resultCount = qs.count()

    context = {
        "queryset" : qs,
        "count" : resultCount
    }

    return render(request, "ase_site/results.html", context)


def posting(request, posting_id):
    """Shows a single posting."""

    posting = Posting.objects.get(posting_id=posting_id)

    context = {
        "posting" : posting
    }

    return render(request, 'ase_site/posting.html', context)


def new_post(request): 
    """Add new job post."""

    if request.method != "POST":
        #No data submitted; render new post form 
        form = SubmitPosting()

        #Display a blank or invalid form 
        context = { "form": form}
        return render(request, "ase_site/new_post.html", context)
        
    else: 
        #POST Data submitted; process data
        form = SubmitPosting(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("ase_site:index")



