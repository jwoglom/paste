from django.shortcuts import render, redirect
from paste.text.models import Author, Paste
import hashlib

def get_author(authorname, oldauthor=None):
    if oldauthor is not None:
        if len(Paste.objects.filter(author__name=oldauthor)) < 2:
            a = Author.objects.get(name=oldauthor)
            a.name = authorname
            a.save()
            return a
    try:
        a = Author.objects.get(name=authorname)
    except Author.DoesNotExist:
        a = Author.objects.create(name=authorname)
        return get_author(authorname)
    return a

def add_view(request):
    if 'confirm' in request.POST:
        author = request.POST.get('author')
        try:
            a = Author.objects.get(name=author)
        except Author.DoesNotExist:
            a = Author.objects.create(name=author)
        p = Paste.objects.create(
            title=request.POST.get('title',''),
            contents=request.POST.get('contents',''),
            author=a,
            private=('private' in request.POST),
            code=('code' in request.POST),
            identifier=""
        )
        p.identifier = hashlib.sha1("{}-{}".format(p.id, p.title)).hexdigest()[:5]
        p.save()
        return redirect("/p/{}".format(p.identifier)) 
    else:
        return render(request, "add.html", {"request": request})

def edit_view(request, paste_id):
    if 'confirm' in request.POST:
        p=Paste.objects.get(identifier=paste_id)
        for k,v in request.POST.items():
            if k not in ('confirm','csrfmiddlewaretoken','author'):
                setattr(p, k, v)
        if 'author' in request.POST:
            p.author = get_author(request.POST.get('author'), p.author)
        p.save()
    return render(request, "view.html", {
        "request": request,
        "paste": Paste.objects.get(identifier=paste_id),
        "ok": ('confirm' in request.POST)
    })
