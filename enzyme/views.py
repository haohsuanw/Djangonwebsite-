import json

from django.db.models.functions import Lower
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import auth
from actions.models import Action
from django.contrib import messages
from django.shortcuts import render
from enzyme import models
from .models import comment,work
from django.contrib.auth.models import User
from datetime import date
import requests


from django.core import serializers


# Create your views here.

#home view homepage
def enzyme_office_home(request):
    actions=Action.objects.all()
    return render(request, "enzymeoffice/enzyme/Home.html",{"actions":actions})

#home view dashboard page
def enzyme_office_dashboard(request):
    usercomment = []
    commentlist = comment.objects.all()




    for comments in commentlist:
        if comments.username==request.session['username']:
            usercomment.append(comments)


    if len(usercomment)==0:
        usercomment= "x"
    if len(commentlist)==0:
        commentlist= "x"


    if  request.session['is_login'] is True:
        if len(commentlist)>0 and request.session['role']=='admin':
            return render(request, "enzymeoffice/enzyme/dashboard.html", {"commentlist": commentlist})


        elif len(commentlist)>0:
            return render(request, "enzymeoffice/enzyme/dashboard.html", {"commentlist": usercomment})
        else:
            return render(request, "enzymeoffice/enzyme/nocomment.html")
    else:
        enzyme_office_alternative

#listpage
def enzyme_office_list(request):
    if request.method == 'GET':
        order_by = request.GET.get('order_by')

        worklist=work.objects.all().order_by(order_by)


    return render(request,"enzymeoffice/enzyme/List.html", {"worklist": worklist})
#detailpage
def enzyme_office_listdetail(request,id):
    worklist = work.objects.all()

    workdetail=[]
    test="this is test"
    for i in range(len(worklist)):
        if int(worklist[i].id) is id:

            workdetail.append(worklist[i])
    print(workdetail[0].id)

    return render(request,"enzymeoffice/enzyme/Listdetail.html", {"workdetail": workdetail,"test":test})
#addpage
def enzyme_office_Add(request,id):
    worklist = work.objects.all()

    workdetail=[]
    if  request.session['is_login'] is True:
        for i in range(len(worklist)):
            if int(worklist[i].id) is id:
                workdetail.append(worklist[i])
        return render(request,"enzymeoffice/enzyme/Add.html", {"workdetail": workdetail})
    else:
        enzyme_office_alternative

#savecomment
def savecomment(request):

    is_ajax=request.headers.get('x-requested-with') == 'XMLHttpRequest'
    commentlist = models.comment.objects.all().order_by('id')

    if is_ajax and request.method == "POST" and request.session['is_login']:
        title = request.POST.get('work')
        try:
            a = request.POST
            id = request.POST['id']
            ide = str(id)
            age = request.POST['age']
            name = request.POST['name']

            workhere = request.POST['work']
            comment = request.POST['text']
            username = request.session['username']
            id = commentlist[len(commentlist)-1].id +1
            nc = models.comment(
                name=name,
                Age=age,
                id=id,
                work=workhere,
                username=username,
                comment=comment,
                date_posted=date.today()
            )
            nc.save()#save to database
            user=User.objects.get(username=request.session.get("username"))

            #log the action
            action=Action(
                user=user,
                verb="created the new comment",
                target=nc
            )
            action.save()


            messages.add_message(request, messages.SUCCESS, "You successfuly submit your comment")
            # meassage


            # Azure Translator

            worklocation=work.objects.get(title=workhere).country
            if worklocation=="Russian":
                endpoint='https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from=en&to=ru'
            elif worklocation=="Thai":
                endpoint='https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from=en&to=th'
            elif worklocation=="Japan":
                endpoint='https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from=en&to=ja'

            headers = {
                # Request headers
                'Content-Type': 'application/json; charset=UTF-8',
                'Ocp-Apim-Subscription-Key': 'aadbb069b24b45a3807f56b5b2357af6',
            }

            body = [{
                'text': comment
            }]

            respons=requests.post(endpoint,headers=headers,json=body)
            respons_json=respons.json()

            aftersave = []

            if type(respons_json) is dict:
                #prevent error
                commentlist = models.comment.objects.filter(work=workhere).order_by('id')
                for comments in commentlist:
                    aftersave.append(comments.name + " : " + comments.comment)
                aftersave.append("you save successfully, but somethings wrong with the Microsoft Azure")
            else:
                langcomment = respons_json[0]['translations'][0]['text']

                commentlist = models.comment.objects.filter(work=workhere).order_by('id')
                for comments in commentlist:
                    if comments.comment == comment:
                        aftersave.append(comments.name + " : " + comments.comment+" Author's Language: "+langcomment)
                    else:
                        aftersave.append(comments.name + " : " + comments.comment)



            return JsonResponse({'success': 'success', 'commentlist': aftersave}, status=200)


        except models.comment.DoesNotExist:
            return JsonResponse({'error': 'No comment with the work'}, status=200)
    else:
        return JsonResponse({'error': 'Invaild Ajax request'}, status=400)




#searchresult page
def enzyme_office_searchresult(request):
    return render(request,"enzymeoffice/enzyme/searchresult.html")
#alternative page
def enzyme_office_alternative(request):
    return render(request,"enzymeoffice/enzyme/Alternativepage.html")

#editpage
def enzyme_office_edit(request,id):
    commentlist = models.comment.objects.all()

    if  request.session['is_login'] is True:
        a=request.POST
        if request.method == 'POST':
            name=request.POST['name']
            Age=request.POST['age']
            comments = request.POST['commentedit']
            id = request.POST['id']
            for comment in commentlist:
                if comment.id==int(id):
                    if (comment.comment != comments):
                        # log the action
                        user = User.objects.get(username=request.session.get("username"))
                        action = Action(
                            user=user,
                            verb="Edit the comment's comment",
                            target=comment
                        )
                        action.save()

                    comment.comment=comments

                    if (comment.name!=name):
                        # log the action
                        user = User.objects.get(username=request.session.get("username"))
                        action = Action(
                            user=user,
                            verb="Edit the commenter",
                            target=comment
                        )
                        action.save()
                    comment.name=name
                    if (comment.Age!=Age):
                        # log the action
                        user = User.objects.get(username=request.session.get("username"))
                        action = Action(
                            user=user,
                            verb="Edit the commenter AGE",
                            target=comment
                        )
                        action.save()
                    comment.Age=Age

                    comment.save()



            messages.add_message(request,messages.INFO,"You successfuly edit your comment")

            return enzyme_office_dashboard(request)
        editcomment = []
        #get target comment and edit it
        for i in range(len(commentlist)):
            if int(commentlist[i].id) is id:
                editcomment.append(commentlist[i])

        return render(request, "enzymeoffice/enzyme/edit.html", {"editlist": editcomment})
    else:
        enzyme_office_alternative(request)


#delete page
def enzyme_office_delete(request,id):
    commentlist = models.comment.objects.all()


    #check the user is admin or not
    if  request.session['is_login'] is True and request.session['role']== 'admin':
        if request.method == 'POST':

            id = request.POST['id']
            id=int(id)


                # log the action


            # log the action
            user = User.objects.get(username=request.session.get("username"))
            action = Action(
                user=user,
                verb="delete one of the comment",
                target=None
            )
            action.save()
            models.comment.objects.filter(id=id).delete()






            messages.add_message(request,messages.WARNING,"You successfuly delete your comment")


            return enzyme_office_dashboard(request)
        deletecomment = []
        for comment in commentlist:
            if int(comment.id) is id:
                deletecomment.append(comment)
                return render(request, "enzymeoffice/enzyme/delete.html", {"editlist": deletecomment})

    else:
        enzyme_office_dashboard(request)





def enzyme_office_loadcomment(request):


    is_ajax=request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method=="POST":
        title=request.POST.get('work')
        try:
            commentlist= models.comment.objects.filter(work=title).order_by('date_posted')
            loadcomment=[]
            user=[]
            time=[]
            for comment in commentlist:
                user.append(comment.username)
                time.append(str(comment.date_posted))
                loadcomment.append(":"+comment.comment)

            return JsonResponse({'success':'success','commentlist':loadcomment,'userlist':user,'timelist':time},status=200)
        except models.comment.DoesNotExist:
            return JsonResponse({'error':'No comments yet'},status=200)
    else:
        return JsonResponse({'error': 'Invaild Ajax request'}, status=400)

