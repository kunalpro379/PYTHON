from django.http import HttpResponse
 # def index():
 #     return "Hey kunal"

# def index(request):
#      return HttpResponse("Hey kunal")
# def index(request):
#      return HttpResponse('''<h1>Hey kunal</h1><a href= "www.google.com"> Django Test</a>''')

def index(index):
     return HttpResponse("INDEX")
def removepunc(request):
     return HttpResponse("remove punc")
def capitalize(request):
     return HttpResponse("capitalizee")