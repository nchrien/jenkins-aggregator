# from django.shortcuts import render
from django.views import generic

from .models import Commit, ResultSet, TestResult

class IndexView(generic.ListView):
    template_name = "aggregator/index.html"
    context_object_name = "latest_commit_list"

    def get_queryset(self):
        return Commit.objects.order_by("-triggerTime")[:5]
        

class CommitView(generic.DetailView):
    model = Commit
    template_name = "aggregator/commit.html"
    
class ResultSetView(generic.DetailView):
    model = ResultSet
    template_name = "aggregator/resultset.html"