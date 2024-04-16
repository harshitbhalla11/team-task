
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Group
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from .models import Group, Task
from django.forms.models import model_to_dict
import json
from django.shortcuts import render, redirect, get_object_or_404
# import boto3
from django.conf import settings
from ses_mail.send_ses import SESEmailService

def landing_page(request):
    return render(request, 'landing-page.html')

def home_page(request):
    return render(request, 'home-page.html')



def add_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group_members = request.POST.getlist('selected_users')
        visibility_type = request.POST.get('visibility')
        description = request.POST.get('description')
        admin_user_id = request.user.id
        admin_user_name = request.user.username

        Group.objects.create(
            group_name=group_name,
            group_members=group_members,
            visibility_type=visibility_type,
            description=description,
            admin_user_id=admin_user_id,
            admin_user_name = admin_user_name
        )
        return redirect('fetch_groups') 
    else:
        return render(request, 'create_group.html')
    
    
def update_group(request, group_id):
    group = Group.objects.get(pk=group_id) 

    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group_members = request.POST.getlist('selected_users')
        visibility_type = request.POST.get('visibility')
        description = request.POST.get('description')

        group.group_name = group_name
        group.visibility_type = visibility_type
        group.description = description
        
        if group_members:
            group.group_members = group_members

        group.save()
        
        return redirect('group_detail',group_id=group_id)  
    else:
        return render(request, 'group_edit.html', {'group_data': group})    



def add_task(request, group_id):
    if request.method == 'POST':
        task_brief = request.POST.get('task_brief')
        description = request.POST.get('description')
        assigned_to = request.POST.getlist('selected_member')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        # labels = request.POST.get('labels')
        groupId = group_id
        created_by = request.user.id
        created_by_name = request.user.username
        attachments = request.FILES.get('file')
        s3_url = None

        # if attachments:
        #     s3_url = upload_file_to_s3(attachments)
         

        Task.objects.create(
            task_brief=task_brief,
            description=description,
            assigned_to=assigned_to,
            due_date=due_date,
            priority=priority,
            status=status,
            # labels=labels,
            group_id=groupId,
            created_by=created_by,
            created_by_name=created_by_name,
            s3_url=s3_url,
            attachments=attachments
        )

        return redirect('group_detail',group_id=group_id)  

# def upload_file_to_s3(file_obj):
#     s3 = boto3.client('s3',
#                       aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#                       aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

#     s3.upload_fileobj(file_obj, settings.AWS_STORAGE_BUCKET_NAME, file_obj.name)

#     s3_url = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{file_obj.name}"

#     return s3_url
    
def fetch_groups(request):
    group_table_data = Group.objects.all()
    return render(request, 'groups.html', {'groups_data': group_table_data})


def group_info(request, group_id):
    group = Group.objects.get(pk=group_id)  
    tasks = Task.objects.filter(group_id=group_id)
    for task in tasks:
        assigned_to_list = json.loads(task.assigned_to[0])
        task.assigned_to = assigned_to_list
    
    group_members_list = json.loads(group.group_members[0])
    group.group_members = group_members_list
    
    return render(request, 'group_detail.html', {'group_data': group, 'tasks_data': tasks, 'group_id': group_id})

def group_edit(request, group_id):
    group = Group.objects.get(pk=group_id)  
    return render(request, 'group_edit.html', {'group_data': group})

def fetch_group_data(request, group_id):
    group = Group.objects.get(pk=group_id)
    group_dict = model_to_dict(group)
    return JsonResponse({'group_data':group_dict}, safe= False)

def group_delete(request, group_id):
    group = Group.objects.get(pk=group_id)
    group.delete()
    return redirect('fetch_groups')

def createtask_view(request,group_id):
     group_data = Group.objects.get(pk=group_id)
     return render(request, 'task/createtask.html',{'group_id':group_id,'group_data':group_data})

def fetch_group_task(request, group_id):
    tasks = Task.objects.filter(group_id=group_id).values()    
    tasks_list = list(tasks)
    return JsonResponse(tasks_list, safe=False)


def my_tasks(request):
    tasks = Task.objects.all()
    for task in tasks:
        assigned_to_list = json.loads(task.assigned_to[0])
        task.assigned_to = assigned_to_list

    tasks_assigned_to_curr_user=[]
    curr_user_id=request.user.id

    for task in tasks:
        for assigned_to_item in task.assigned_to:
            if assigned_to_item['id'] == curr_user_id:
                tasks_assigned_to_curr_user.append(task)
                break

    return render(request, 'myTask/task_detail.html', {'task_data': tasks_assigned_to_curr_user,'user_id':curr_user_id})

def update_task(request,task_id):
    task = Task.objects.get(pk=task_id) 

    if request.method == 'POST':
        task_brief = request.POST.get('task_brief')
        description = request.POST.get('description')
        assigned_to = request.POST.getlist('selected_member')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        # labels = request.POST.get('labels')
        groupId = task.group_id
        created_by = request.user.id
        created_by_name = request.user.username
        attachments = request.FILES.get('file')
        s3_url = 'NA'

        # if attachments:
        #     s3_url = upload_file_to_s3(attachments)
         

        task.task_brief = task_brief
        task.description = description
        task.assigned_to = assigned_to
        task.due_date = due_date
        task.priority = priority
        task.status = status
        # task.labels = labels
        task.group_id = groupId
        task.created_by = created_by
        task.created_by_name = created_by_name
        task.s3_url = s3_url
        task.attachments = attachments

        task.save()
        
        return redirect('myTask')  
    else:
        return render(request, 'task/edit_task.html', {'task_data': task})

def edit_task(request,task_id):
    task = Task.objects.get(pk=task_id) 
    return render(request, 'task/edit_task.html', {'task_data': task})