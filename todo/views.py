# Create your views here.
from todo.models import *
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

@staff_member_required
def mark_done(request, pk):
    item = Items.objects.get(pk=pk)
    item.done = True
    item.save()
    return HttpResponseRedirect(reverse('todo.views.mark_done2', args=(pk,)))

def mark_done2(request, pk):
    return HttpResponse("maskdone2")

@staff_member_required
def item_action(request, action, pk):
    """Mark done, toggle onhold or delete a todo item."""
    if action == "done":
        item = Item.objects.get(pk=pk)
        item.done = True
        item.save()
    elif action == "onhold":
        item = Item.objects.get(pk=pk)
        if item.onhold: item.onhold = False
        else: item.onhold = True
        item.save()
    elif action == "delete":
        Item.objects.filter(pk=pk).delete()

    return HttpResponseRedirect(reverse("admin:todo_item_changelist"))