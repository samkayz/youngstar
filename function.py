from user.models import *
from django.contrib import messages



class Main:
    #Function to add Question into the Database
    def create_question(self, request, questn, option1, option2, option3, option4, answer):
        create = Question(questn=questn, option1=option1, option2=option2, option3=option3, option4=option4, answer=answer)
        create.save()
        return messages.success(request, "Question Added Succesfully")


    #Function to Show All Questions in a Table
    def show_all_question(self):
        show = Question.objects.filter()
        return show


    #Function to Edit Question
    def edit_question(self, id):
        all_info = Question.objects.all().get(id=id)
        return all_info

    #Function to Update Question
    def update_question(self, request, id, questn, option1, option2, option3, option4, answer):
        Question.objects.filter(id=id).update(questn=questn, option1=option1, option2=option2, option3=option3, option4=option4, answer=answer)
        return messages.success(request, "Question Updated Succesfully")
    
    #Function to Delete Question
    def delete_question(self, request, id):
        Question.objects.filter(id=id).delete()
        return messages.success(request, "Question Deleted")
    
    #Function to Add Story
    def add_story(self, request, story):
        add = Story(story=story)
        add.save()
        return messages.success(request, "Story Added")

    #Function to Delete Story
    def delete_story(self, request, id):
        Story.objects.filter(id=id).delete()
        return messages.success(request, "Story Deleted")
    

    def all_story(self):
        show = Story.objects.filter()
        return show
    