from django.shortcuts import *
from function import *
from django.db.models import Sum

Object = Main()

def index(request):
    show = Object.show_all_question()
    show_story = Object.all_story()
    return render(request, 'index.html', {'show': show, 'show_story': show_story})

#View fuction that handle question
def add_question(request):
    if request.method == "POST":
        question = request.POST['question']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']
        option4 = request.POST['option4']
        answer = request.POST['answer']

        Object.create_question(request, question, option1, option2, option3, option4, answer)
        return redirect('/add')
    else:
        show = Object.show_all_question()    
        return render(request, 'add_question.html', {'show': show})


#View fuction that handle question update
def update(request, id):
    if request.method == "POST":
        question = request.POST['question']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']
        option4 = request.POST['option4']
        answer = request.POST['answer']

        Object.update_question(request, id, question, option1, option2, option3, option4, answer)
        return redirect('/add')

#View fuction that handle processing of the result
def process(request):
    total = Question.objects.all()
    N = len(total)
    allData = []
    for i in range(N):
        mu = i + 1
        value = request.POST.get(f'radio{mu}')
        if value == None: continue
        id = value[0]
        cardData = {}
        cardData['id'] = value[0]
        cardData['option'] = value[1:]
        allData.append(cardData)
    

    tot = []
    for i, data in enumerate(allData):
        answer = Question.objects.all().get(id=data['id'])
        if answer.answer == data['option']:
            k = 1 * 5
            tot.append(k)
            
    sum_total = sum(tot)
    sum_of_question = (N * 5)

    percentage = float((sum_total * 100) / sum_of_question)
    return render(request, 'finish.html', {'percentage': round(percentage)})


#View fuction that handle delete
def delete(request, id):
    Object.delete_question(request, id)
    return redirect('/add')


#View fuction that handle question editting
def edit_question(request, id):
    all_info = Object.edit_question(id)
    show = Object.show_all_question()
    return render(request, 'edit_question.html', {'all_info': all_info, 'show': show})


#View fuction that handle question Updating
def update_question(request):
    if request.method == "POST":
        id = request.POST['id']
        question = request.POST['question']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']
        option4 = request.POST['option4']
        answer = request.POST['answer']

        Object.update_question(request, id, question, option1, option2, option3, option4, answer)
        return redirect('/add')

#View fuction that handle Adding story Story
def add_story(request):
    if request.method == "POST":
        story = request.POST['story']
        Object.add_story(request, story)
        return redirect('/add_story')
    
    show = Object.all_story()
    return render(request, 'add_story.html', {'show': show})

#View fuction that handle Adding story Story
def delete_story(request, id):
    Object.delete_story(request, id)
    return redirect('/add_story')