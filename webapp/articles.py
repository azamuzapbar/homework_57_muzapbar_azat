from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, FormView
from webapp.models import Task
from webapp.forms import TaskForm


def add_view(request):
    form = TaskForm()
    if request.method == 'GET':
        context = {
            'form': form
        }
        print(context)
        return render(request, 'article_create.html', context)
    form = TaskForm(request.POST)
    if not form.is_valid():
        context = {
            'form': form
        }
        return render(request, 'article_create.html', context)
    task = form.save()
    return redirect('article_detail', pk=task.pk)


class ArticleView(TemplateView):
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class ArticleUpdateView(TemplateView):
    template_name = 'article_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        context['form'] = TaskForm(instance=context['task'])
        return context

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=task.pk)
        return render(request, 'article_update.html', context={'task': task, 'form': form})




def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'article_confirm_delete.html', context={'task': task})


def confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')
