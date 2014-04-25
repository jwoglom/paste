from django.shortcuts import render
from paste.text.models import Author, Paste
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
            code=('code' in request.POST)
        )
        return redirect("/p/{}".format(p.id)) 
    else:
        return render(request, "add.html", {"request": request})

def edit_view(request, paste_id):
    if 'confirm' in request.POST:
        p=Paste.objects.get(id=paste_id)
        for k,v in request.POST.items():
            setattr(p, k, v)
        p.save()
    return render(request, "view.html", {
        "request": request,
        "paste": Paste.objects.get(id=paste_id)
    })
