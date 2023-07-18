from django.contrib import admin
from . import models
from .models import AboutUs, Core, Module,  Enquiry, Feedback, CoreDescription, ModuleDescription
import django.apps
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin
# from django.db.models import getModels, getApps
from django.contrib.admin.sites import AlreadyRegistered

def autoregister(*app_list):
    models = django.apps.apps.get_models()
    for model in models:
        try:
            cadd_site.register(model)
        except AlreadyRegistered:
            pass



# Register your models here.


class CaddAdminArea(admin.AdminSite):
    site_header = 'CADD ADMIN'
    login_template = 'caddadmin/login.html'
    index_template = 'caddadmin/index.html'

  
cadd_site = CaddAdminArea(name='caddAdmin')

class MembershipInline(admin.TabularInline):
    model = Module.cores.through
    extra = 0
    search_fields = ['core']
    autocomplete_fields = ['core']

class coreDescriptionInline(SummernoteInlineModelAdmin, admin.StackedInline):
    model = CoreDescription
    extra = 0

class moduleDescriptionInline(SummernoteInlineModelAdmin, admin.StackedInline):

    model = ModuleDescription
    extra = 0


    


class coreAdmin(admin.ModelAdmin):
    list_display = ['coreName', 'coreSlug']

    search_fields = ["corename"]
    inlines = [
        coreDescriptionInline, 
        MembershipInline 
    ]
    # summernote_fields = '__all__'

    



class moduleAdmin(admin.ModelAdmin, ):
    list_display =['moduleName', 'moduleSlug', 'moduleImage']
    search_fields = ["modulename"]
    inlines = [
        moduleDescriptionInline, 
        MembershipInline,
    ]

class enquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject']

class feedbackAdmin(admin.ModelAdmin):
    list_display = ['qualityOfTraining', 'qualityOfTrainer', 'qualityOfTrainingMaterials', 'overallExperience']


class topStreamDescriptionAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display =['descriptionTitle','logoImage']


cadd_site.register(AboutUs , SummernoteModelAdmin )
cadd_site.register(Core, coreAdmin )
cadd_site.register(Module, moduleAdmin)
cadd_site.register(Enquiry, enquiryAdmin)
cadd_site.register(Feedback, feedbackAdmin)
# cadd_site.register(ModuleDescription, SummernoteModelAdmin)
cadd_site.register(models.TopStreamDescription, topStreamDescriptionAdmin)



autoregister('myapp')






# cadd_site.register(coreDescription, )









# class courseIndexAdmin(admin.StackedInline):
#     model = models.CourseIndex
#     extra = 3

# class courseGroupAdmin(admin.ModelAdmin):
#     fields = ['courseGroupName'] 
#     inlines = [courseIndexAdmin]

# # class CourseDescriptionAdmin(admin.StackedInline):
# #     model = models.courseDescription
# #     extra = 3

# # class CourseIndexAdmin(admin.ModelAdmin):
# #     fields = ['courseName']
# #     inlines = [CourseDescriptionAdmin]

# # class SubCourseDescriptionAdmin(admin.StackedInline):
# #     model = models.subCourseDescription
# #     extra = 3

# # class subCourseIndexAdmin(admin.ModelAdmin):
# #     fields = ['subCourseName']
# #     inlines = [SubCourseDescriptionAdmin]

# # class courseContentDescriptionAdmin(admin.StackedInline):
# #     model = models.courseContentDescription
# #     extra = 2

# # class courseContentTitleAdmin(admin.StackedInline):
# #     model = models.courseContentTitle
# #     # fields = ['contentTitle']
# #     extra = 3

# # class courseContentTitleMainAdmin(admin.ModelAdmin):
# #     fields = ['contentTitle']
# #     inlines = [courseContentDescriptionAdmin]
# # class courseIndexAdmin(admin.ModelAdmin):
# #     fields = ['courseName']
# #     inlines = [courseContentTitleAdmin]



# admin.site.register(models.aboutUs)
# # admin.site.register(models.courseDescription)
# # admin.site.register(models.courseIndex,CourseIndexAdmin)
# # admin.site.register(models.subCourseDescription)
# # admin.site.register(models.subCourseIndex, subCourseIndexAdmin)
# admin.site.register(models.testimonial)
# # admin.site.register(models.projects)
# # admin.site.register(models.partners)
# # admin.site.register(models.courseWithSubCourse)
# # admin.site.register(models.courseIndex, courseIndexAdmin)
# # admin.site.register(models.courseContentTitle, courseContentTitleMainAdmin)
# # admin.site.register(models.courseContentDescription)
# # admin.site.register(models.subCourseIndex)
# # admin.site.register(models.subCourseContentTitle)
# # admin.site.register(models.subCourseContentDescription)

# admin.site.register(models.jobOpportunities)



# model_list = django.apps.apps.get_models()
# for model in model_list:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass 

# admin.site.unregister(models.CourseGroup) 

# admin.site.register(models.CourseGroup, courseGroupAdmin)
    

