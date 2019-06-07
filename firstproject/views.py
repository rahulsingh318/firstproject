from django.http import HttpResponse
from django.shortcuts import render
import operator

def index(request):
    return render(request, 'index.html',{'name':'Hii there rahul'})

# def about(request):
#     return HttpResponse('''<a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">About Hello World</a>''')

def count(request):
    data = request.GET['fulltextarea']
    word_list = data.split()
    list_lenght = len(word_list)

    worddictionary = {}
    for word in word_list:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sorted_item = sorted(worddictionary.items(),key =operator.itemgetter(1),reverse = True)

    return render(request,'count.html',{'fulltextarea':data,'words':list_lenght,'worddictionary':sorted_item})

def about(request):
    return render(request,'about.html')


# def analyze(request):
    #Get the text
    # djtext = request.GET.get('text', 'default')

    # Check checkbox values
    # removepunc = request.GET.get('removepunc', 'off')
    # fullcaps = request.GET.get('fullcaps', 'off')
    # newlineremover = request.GET.get('newlineremover', 'off')
    # extraspaceremover = request.GET.get('extraspaceremover', 'off')
    # print(djtext)
    # #Analyze the text
    # return HttpResponse("remove punc")
    

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("capitalize first")


# def spaceremove(request):
#     return HttpResponse("space remover")

# def charcount(request):
#     return HttpResponse("charcount <a href='/'>Back</a>")

