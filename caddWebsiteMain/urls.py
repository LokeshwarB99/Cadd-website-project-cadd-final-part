from django.urls import path
# from .views import (homeView, aboutUsView, contactUsView, coursesView, courseDescriptionView, subCoursesView, subCourseDescriptionView, testimonialsView)
from . import views
from caddWebsiteMain.admin import cadd_site

# urlpatterns = [
#     path('', homeView),
#     path('about/', aboutUsView ), 
#     path('contact/', contactUsView),
#     path('courses/', coursesView), 
#     path('courses/<int:courseId>/', courseDescriptionView),
#     path('subcourses/', subCoursesView ), 
#     path('subcourses/<int:subCourseId>/', subCourseDescriptionView),
#     path('testimonials/', testimonialsView),
# ]

urlpatterns = [
    path('', views.homeView, name='home'),
    path('about/', views.aboutUsView, name='about'),

    path('courseGroup/', views.courseGroupView, name='courseGroup'),
    path('course/<slug:courseGroupSlug>/<slug:courseSlug>/', views.courseDescriptionView, name="courseDescription"),

    path('testimonial/', views.testimonialView, name='testimonial'),
    # path('course/', views.coursesView, name='course'),
    # path('course/<int:courseId>/', views.courseDescriptionView, name='courseDescription'),

    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('contactUs/', views.contactUsview, name='contact'),
    path('feedback/', views.feedbackView, name='feedback'),
    path('jobfair/', views.jobfairview, name='jobfair'),
    path('etc/', views.etcView, name='etc'),
    path('student-value-adds/', views.studentValueAddsView, name='studentValueAdds'),
    path('placement/', views.placementView, name='placement'),
    path('filterPlacement/', views.placementFilterSearchView, name='filterPlacement'),
    path('loadmore/', views.placementLoadMoreView, name='placementLoadMore'),
    # path('testimonial/', views.testimonialView, name='testimonial'),

]