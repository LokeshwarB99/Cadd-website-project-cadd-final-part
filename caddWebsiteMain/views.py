from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
import random
from . import models
# from .models import (aboutUs, courseIndex, courseDescription, subCourseIndex, subCourseDescription, courseWithSubCourse)

# # Create your views here.
def homeView(request):
    template_name = 'home.html'
    topStreamCourse = models.CourseGroup.objects.get(courseGroupSlug='top-stream')
    projectManagementCourse = models.CourseGroup.objects.get(courseGroupSlug = 'project-management')
    productDesignCourse = models.CourseGroup.objects.get(courseGroupSlug = 'product-design-analysis')
    informationTechnologyCourse = models.CourseGroup.objects.get(courseGroupSlug= 'information-technology')
    context = {'topStreamCourse': topStreamCourse, 'projectManagementCourse': projectManagementCourse, 'productDeisgnCourse': productDesignCourse, 
                'informationTechnologyCourse': informationTechnologyCourse}
    return render(request, template_name, context)

def aboutUsView(request):
    template_name = 'aboutUs.html'
    return render(request, template_name)

def privacypolicy(request):
    template_name = 'privacypolicy.html'
    return render(request, template_name)

def courseGroupView(request):
    template_name = 'courseGroup.html'
    objects = models.CourseGroup.objects.all()
    context = {'objects': objects} 
    return render(request, template_name, context) 
    
# def coursesView(request):
#     template_name = 'courses.html'
#     objects = models.CourseIndex.objects.all()
#     context = {'objects':objects}
#     return render(request, template_name, context) 

def contactUsview(request):
    if request.method == 'POST':
        try:
            
            obj = models.Enquiry()
            obj.name = request.POST['name']
            obj.email = request.POST['email']
            validate_email(obj.email)
            obj.phone = request.POST['phone']
            obj.subject = request.POST['subject']
            obj.save()
            context = {'result':'Your form got submitted successfully!'}
        except:
            pass
        messages.info(request, "Your form got submitted successfully");
        return redirect('/')
    template_name = 'contactus.html'
    return render(request, template_name)
# def courseDescriptionView(request, courseId):
#     template_name = 'courseDescription.html'
#     courseName = models.CourseIndex.objects.get(pk = courseId)
#     contentTitle = models.CourseContentTitle.objects.filter(courseId = courseId)

#     context = {'courseName':courseName, 'contentTitle':contentTitle}
#     return render(request, template_name, context)
    
# def subCoursesView(request):
#     template_name = 'subCourse.html'
#     objects = subCourseIndex.objects.all()
#     context = {'objects':objects}
#     return render(request, template_name, context)
    
# def courseDescriptionView(request, courseId):
#     template_name = 'courseDescription.html'
#     courseName = courseIndex.objects.get(pk = courseId).courseName
#     objects = courseDescription.objects.filter(courseId=courseId)
    
#     subCoursesGroup = courseWithSubCourse.objects.filter(courseId=courseId)

#     subCoursesList ={}
#     for items in subCoursesGroup:

#         subCourseId = items.subCourseId.pk
#         subCourseName = subCourseIndex.objects.get(pk = subCourseId).subCourseName
#         subCoursesList[subCourseId] = subCourseName
    
#     print(subCoursesList)
    
#     context = {'objects': objects, 'courseName': courseName, 'subCoursesList': subCoursesList}
#     return render(request, template_name, context)
    
# def subCourseDescriptionView(request, subCourseId):
#     template_name = 'subCourseDescription.html'
#     objects = subCourseDescription.objects.filter(subCourseId=subCourseId)
#     subCourseName = subCourseIndex.objects.get(pk = subCourseId).subCourseName
#     context = {'objects': objects, 'subCourseName': subCourseName}
#     return render(request, template_name, context)

def courseDescriptionView(request, courseGroupSlug, courseSlug):

    courseGroupName = models.CourseGroup.objects.get(courseGroupSlug=courseGroupSlug).courseGroupName
    if courseGroupName == 'Our Courses':
        template_name = 'certificateCourses.html'
        course = models.Core.objects.get(coreSlug = courseSlug)
    elif courseGroupName == 'Top Stream':
        template_name = 'topStreamCourses.html'
        course = models.Core.objects.get(coreSlug = courseSlug)

    else:
        template_name = 'generalCourses.html'
        course = models.Module.objects.get(moduleSlug = courseSlug)
        
    
    # courseName = models.CourseIndex.objects.get(pk = courseId)
    # contentTitle = models.CourseContentTitle.objects.filter(courseId=courseId)
    context = {'courseGroupName': courseGroupName, 'course':course} 
    return render(request, template_name, context)
    
def testimonialView(request):
    template_name = 'testimonial.html'
    testimonialObjects = models.Testimonial.objects.all()
    context = {'objects':testimonialObjects}
    return render(request, template_name, context)
    


# def enquiryView(request):
#     if request.method == 'GET':
#         template_name = 'enquiry.html'
#         if 'context' in request.session:
#             context = request.session['context']
#             del request.session['context']
#         else:
#             context = {}
#         choice = random.randint(9, 100)
#         context['choice'] = choice
#         return render(request, template_name, context)
    
#     elif request.method == 'POST':
#         try:
            
#             obj = models.Enquiry()
#             obj.name = request.POST['name']
#             obj.email = request.POST['email']
#             validate_email(obj.email)
#             obj.phone = request.POST['phone']
#             obj.subject = request.POST['subject']
#             obj.save()
#             context = {'result':'Your form got submitted successfully!'}
#         except ValueError as v:
#             message = str(v.message)
#             context = {'result':message}
            
#         except ValidationError as validationError:
#             context = {'result':'Enter a valid Email address...'}
#         request.session['context'] = context
            
#         return redirect('enquiry')


   
def feedbackView(request):
    if request.method == 'GET':
        template_name = 'feedback.html'
        if 'context' in request.session:
            context = request.session['context']
            del request.session['context']
        else:
            context = {}
        return render(request, template_name, context)
    
    elif request.method == 'POST':
        try:
            
            obj = models.Feedback()
            obj.qualityOfTraining = int(request.POST['quality-of-instruction'])
            obj.qualityOfTrainer = int(request.POST['quality-of-trainer'])
          
            obj.qualityOfTrainingMaterials = int(request.POST['quality-of-trainingMaterials'])
            obj.overallExperience = int(request.POST['overal-experience'])
            obj.save()
            context = {'result':'Your form got submitted successfully!'}
        except:
            
            context = {'result':"Your feedback has not been taken due to some technical issues...."}

        request.session['context'] = context
            
        return redirect('feedback')

def jobfairview(request):
    template_name = 'jobfair.html'
    return render(request, template_name) 

def etcView(request):
    template_name = 'etc.html'
    return render(request, template_name)

def studentValueAddsView(request):
    template_name = 'studentValueAdds.html'
    return render(request, template_name)

def placementView(request):
    template_name = 'placement.html'
    placementObjects = models.JobOpportunities.objects.all()[:1]
    totalObjects = models.JobOpportunities.objects.count()
    categoryObjects = models.JobOpportunities.objects.values('category').distinct()
    educationObjects = models.JobOpportunities.objects.values('education').distinct()
    locationObjects = models.JobOpportunities.objects.values('mainLocation').distinct()
    context = {'object': placementObjects, 'totalObject':totalObjects, 'categoryObjects':categoryObjects,
                'educationObjects':educationObjects, 'locationObjects':locationObjects}
    return render(request, template_name, context)

def placementFilterSearchView(request):
    
    categoryValue = request.GET.get("categoryValue")
    departmentValue = request.GET.get("departmentValue")
    locationValue = request.GET.get("locationValue")
    if categoryValue is None:
        categoryValue =''
    if departmentValue is None:
        departmentValue = ""
    if locationValue is None:
        locationValue =""
    placementObjects = list(models.JobOpportunities.objects.filter(category__icontains = categoryValue, education__icontains = departmentValue, mainLocation__icontains = locationValue).values())[:1]
    totalLength = len(placementObjects)
    data = {'objects': placementObjects, 'totalLength': totalLength}
    print(placementObjects)
    return JsonResponse(data=data, encoder=DjangoJSONEncoder, safe=False)


def placementLoadMoreView(request):
    loadedItemLength = request.GET.get('loadedItemLength')
    categoryValue = request.GET.get("categoryValue")
    departmentValue = request.GET.get("departmentValue")
    locationValue = request.GET.get("locationValue")
    if categoryValue is None:
        categoryValue =''
    if departmentValue is None:
        departmentValue = ""
    if locationValue is None:
        locationValue =""
    loadedItemLength = int(loadedItemLength)
    limit = 1
    placement_objects = list(models.JobOpportunities.objects.filter(category__icontains = categoryValue, education__icontains = departmentValue, mainLocation__icontains = locationValue).values()[loadedItemLength:loadedItemLength+limit])
    data = {'objects':placement_objects}
    print(data)
    return JsonResponse(data = data, encoder=DjangoJSONEncoder, safe=False)

# def placementFilterSearchView(request):
#     pass




