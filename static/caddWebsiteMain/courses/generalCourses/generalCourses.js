const relatedCourses = document.querySelectorAll('.CADD-courses-related_courses ul li span');
const array = Array.prototype.slice.call(relatedCourses);

array.map((certificateCourse)=>{
    certificateCourse.addEventListener('click', ()=>{
        if(certificateCourse.innerHTML=="Proficient")
        window.location.href = '/course/our-courses/proficient-level';
        else if(certificateCourse.innerHTML=="Masters"){
            window.location.href='/course/our-courses/master-level';
        }else{
            window.location.href='/course/our-courses/expert-level';
        }
    });
});