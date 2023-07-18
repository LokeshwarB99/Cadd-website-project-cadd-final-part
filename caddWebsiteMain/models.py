from django.db import models
from datetime import datetime 

from django.utils.text import slugify

# class CourseGroup(models.Model):
#   courseGroupName = models.CharField(max_length=255)

# class CourseIndex(models.Model):
#   courseGroupId = models.ForeignKey(CourseGroup, on_delete=models.SET_NULL, null=True)
#   courseName = models.CharField(max_length = 100)

#   def __str__(self):
#     return self.courseName

# class CourseContentTitle(models.Model):
#   courseId = models.ForeignKey(CourseIndex, on_delete = models.CASCADE)
#   courseContentTitle = models.CharField(max_length=100)
  
# class CourseContentDescription(models.Model):
#   courseContentTitleId = models.ForeignKey(CourseContentTitle, on_delete = models.CASCADE)
#   courseContentDescription = models.TextField()



# class SubCourseIndex(models.Model):
#   subCourseName = models.CharField(max_length = 100)

#   def __str__(self):
#     return self.subCourseName
  
# class SubCourseContentTitle(models.Model):
#   subCourseId = models.ForeignKey(SubCourseIndex, on_delete = models.CASCADE)
#   subCourseContentTitle = models.CharField(max_length=100)

# class SubCourseContentDescription(models.Model):
#   subCourseContentTitleId = models.ForeignKey(SubCourseContentTitle, on_delete=models.CASCADE)
#   subCourseContentDescription = models.TextField()

# class CourseWithSubCourse(models.Model):
#   courseId = models.ForeignKey(CourseIndex, on_delete=models.CASCADE)
#   subCourseId = models.ForeignKey(SubCourseIndex, on_delete=models.CASCADE)



class CourseGroup(models.Model):
  courseGroupName = models.CharField(max_length=255)
  courseGroupSlug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

  def save(self, *args, **kwargs):
    if not self.courseGroupSlug:
      self.courseGroupSlug = slugify(self.courseGroupName)
    super(CourseGroup, self).save(*args, **kwargs)


  def __str__(self):
    return self.courseGroupName





class Core(models.Model):
  courseGroupId = models.ForeignKey(CourseGroup, on_delete=models.SET_NULL, null=True)
  coreName = models.CharField(max_length = 100)
  coreImage = models.ImageField(upload_to='caddWebsiteMain/courseImages/', blank=True, null=True)
  coreSlug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

  def save(self, *args, **kwargs):
    if not self.coreSlug:
      self.coreSlug = slugify(self.coreName)
    super(Core, self).save(*args, **kwargs)

  def __str__(self):
    return self.coreName

class Module(models.Model):
  courseGroupId = models.ForeignKey(CourseGroup, on_delete=models.SET_NULL, null=True)
  moduleName = models.CharField(max_length = 100)
  moduleImage = models.ImageField(upload_to='caddWebsiteMain/courseImages/', blank=True, null=True)
  cores = models.ManyToManyField(Core, related_name='contains', blank=True)  
  moduleSlug = models.SlugField(max_length=255, blank=True, null=True, unique=True)

  def save(self, *args, **kwargs):
    if not self.moduleSlug:
      self.moduleSlug = slugify(self.moduleName)
    super(Module, self).save(*args,**kwargs)

  def __str__(self):
    return self.moduleName
  
class CoreDescription(models.Model):
  core = models.ForeignKey(Core, on_delete = models.CASCADE)
  descriptionTitle = models.CharField(max_length = 100)
  description = models.TextField()

  def __str__(self):
    return self.descriptionTitle

class ModuleDescription(models.Model):
  module = models.ForeignKey(Module, on_delete = models.CASCADE)
  descriptionTitle = models.CharField(max_length = 100)
  description = models.TextField()

  def __str__(self):
    return self.descriptionTitle

class TopStreamDescription(models.Model):
  coreDescriptionId = models.ForeignKey(CoreDescription, on_delete=models.CASCADE, null=True)
  logoImage = models.ImageField(upload_to='courses/', null=True, blank=True)
  descriptionTitle = models.CharField(max_length=255, null=True, blank=True)
  description = models.TextField(blank=True, null=True)






class CaddBasicDetails(models.Model):
  address = models.TextField()
  email = models.CharField(max_length=300)
  youtube = models.CharField(max_length=300)
  facebook = models.CharField(max_length=300)
  twitter = models.CharField(max_length=300)
  instagram = models.CharField(max_length=300)
  linkedin = models.CharField(max_length=300)
  phoneNumber = models.CharField(max_length=100)





class Advertisements(models.Model):
  name = models.CharField(max_length=200)
  banner = models.ImageField(upload_to='advertisements/')
  link = models.CharField(max_length=200)

  def __str__(self):
    return self.name


""" dont touch this below part it is working perfectly"""

class AboutUs(models.Model):
  descriptionTitle = models.CharField(max_length=100)
  description = models.TextField()
  image = models.ImageField(default=None, null=True)

  def __str__(self):
    return str(self.descriptionTitle)
  
# class projects(models.Model):
#   superCourseId = models.ForeignKey(courseIndex, on_delete = models.CASCADE)
#   projectTitle = models.CharField(max_length=100)
#   projectDescription = models.TextField()
  
class Testimonial(models.Model):
  feedback = models.TextField()
  studentName = models.CharField(max_length=100)
  ratings = models.IntegerField()
  
# class Partners(models.Model):
#   productName = models.CharField(max_length=100)
#   description = models.TextField()
#   partnerName = models.CharField(max_length=100)
#   partnerLink = models.CharField(max_length=100)

#   def __str__(self):
#     return str(self.partnerName)


'''This is the finalized correct model for contactUs'''
class Enquiry(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  phone = models.IntegerField()
  subject = models.TextField()

class Feedback(models.Model):
  qualityOfTraining = models.IntegerField()
  qualityOfTrainer = models.IntegerField()
  qualityOfTrainingMaterials = models.IntegerField()
  overallExperience = models.IntegerField()
  

class JobOpportunities(models.Model):
  jobRole = models.CharField(max_length=100)
  companyName = models.CharField(max_length=100)
  location = models.TextField(blank=True)
  mainLocation = models.CharField(max_length=100, null=True, blank=True)
  companyLogo = models.ImageField(upload_to ='images/placements/')
  companyWebsiteLink = models.CharField(max_length=200, blank=True, null=True)
  category = models.CharField(max_length=100)
  salary = models.IntegerField()
  education = models.CharField(max_length=200)
  department = models.CharField(max_length=200, blank=True, null=True)
  experience = models.CharField(max_length=100, blank=True, null=True)
  keyFeatures = models.TextField(blank=True)
  lastDate = models.DateField(null=True)

  def __str__(self):
    return self.jobRole+" "+self.companyName
  


