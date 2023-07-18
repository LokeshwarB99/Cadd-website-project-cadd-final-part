
from . import models


def load_hybridCourses_and_certificateCourses(request):
    hybridCourses = models.CourseGroup.objects.get(courseGroupSlug = 'hybrid-courses')
    certificateCourses = models.CourseGroup.objects.get(courseGroupSlug = 'our-courses')
    return {'hybridCourses':hybridCourses, 'certificateCourses':certificateCourses}


def load_basicDetails(request):
    basicDetails = models.CaddBasicDetails.objects.get(pk=1)
    return {'caddBasicDetails': basicDetails}

def load_advertisements(request):
    advertisements = models.Advertisements.objects.order_by('?')[0:3]
    return {'advertisements':advertisements}