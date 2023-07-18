const loadMoreButton = $("#placement-load-more-btn");
const totalObjects = JSON.parse(document.getElementById("jsonTotal").textContent);

let contentContainer = $(".all-jobs");
// console.log(totalObjects);

const categorySearch =   $("#placementCategory");
const departmentSearch = $("#placementDepartment");
const locationSearch =   $("#placementLocation");



function filterPlacementObjects(){
    let categoryValue =   $("#placementCategory option:selected").val();
    let departmentValue = $("#placementDepartment option:selected").val();
    let locationValue =   $("#placementLocation option:selected").val();
    let jsonTotal = $("#jsonTotal");
    console.log(categoryValue, departmentValue, locationValue);
    $.ajax({
        url: '/filterPlacement',
        type: 'GET',
        data: {
            'categoryValue': categoryValue,
            'departmentValue': departmentValue,
            'locationValue': locationValue,
        },
        success: function(response){
            const data = response['objects'];
            contentContainer.html("");
            data.map(obj => {
                console.log(obj.jobRole);
                contentContainer.append(`<div class="boxes">
                <div class="box-flex">
                    <p>${obj.jobRole}</p>
                    <img src="/media/${obj.companyLogo}" alt="neolite" width="50px">
                </div>
                <div class="loc">
                    <img src="	https://caddcentre.com/assets/images/placement/opportunities-icons/location.svg" width="10px" style="margin-right: 5px;" alt="map">
                    <p>${obj.location}</p>
                </div>
                <div class="sal-last">
                    <div class="sal">
                        <img src="	https://caddcentre.com/assets/images/placement/opportunities-icons/salary.svg" alt="salary" width="15px" style="margin-right: 5px;">
                        <p><b>Salary</b>: ${obj.salary}</p>
                    </div>
                    <div class="last">
                        <img src="https://caddcentre.com/assets/images/placement/opportunities-icons/calendar.svg" alt="calendar" width="15px" style="margin-right: 5px;">
                        <p><b>Last date</b>: ${obj.lastDate}</p>
                    </div>
                </div>
                <div class="sal-last">
                    <div class="sal">
                        <img src="https://caddcentre.com/assets/images/placement/opportunities-icons/job.svg" alt="salary" width="15px" style="margin-right: 5px;">
                        <p><b>Category</b>: ${obj.category}</p>
                    </div>
                    <div class="last">
                        <img src="https://caddcentre.com/assets/images/placement/opportunities-icons/duration.svg" alt="calendar" width="15px" style="margin-right: 5px;">
                        <p><b>Duration</b>: Permanent</p>
                    </div>
                </div>
                <div class="loc">
                    <img src="	https://caddcentre.com/assets/images/placement/opportunities-icons/education.svg" width="15px" style="margin-right: 5px;" alt="map">
                    <p><b>Education</b>: ${obj.education}</p>
                </div>
                <div class="loc">
                    <img src="	https://caddcentre.com/assets/images/placement/opportunities-icons/key-requirements.svg" width="14px" style="margin-right: 5px;" alt="map">
                    <p><b>Key requirements</b>:<br>${obj.keyFeatures}<span style="color:#e31e24;">Know more...</span></p>
                </div>
            </div>`);
            })
            jsonTotal.text(response['totalLength']);
        },
    })
}

function loadMoreObjects(){
    let currentItemLength = $(".boxes").length;
    let contentContainer = $(".all-jobs");
    let categoryValue =   $("#placementCategory option:selected").val();
    let departmentValue = $("#placementDepartment option:selected").val();
    let locationValue =   $("#placementLocation option:selected").val();
    let jsonTotal = $("#jsonTotal");
    $.ajax({
        url: '/loadmore',
        type: 'GET',
        data: {
            'loadedItemLength': currentItemLength,
            'categoryValue': categoryValue,
            'departmentValue': departmentValue,
            'locationValue': locationValue,
        },
        success: function(response){
            const data = response['objects'];
            console.log(data);
            console.log(response);

            data.map(obj => {
                console.log(obj.jobRole);
                contentContainer.append(`<div class="boxes">
                <div class="box-flex">
                    <p>${obj.jobRole}</p>
                    <img src="/media/${obj.companyLogo}" alt="neolite" width="50px">
                </div>
                <div class="loc">
                    <img src="	https://caddcentre.com/assets/images/placement/opportunities-icons/location.svg" width="10px" style="margin-right: 5px;" alt="map">
                    <p>${obj.location}</p>
                </div>
                <div class="sal-last">
                    <div class="sal">
                        <img src="	https://caddcentre.com/assets/images/placement/opportunities-icons/salary.svg" alt="salary" width="15px" style="margin-right: 5px;">
                        <p><b>Salary</b>: ${obj.salary}</p>
                    </div>
                    <div class="last">
                        <img src="https://caddcentre.com/assets/images/placement/opportunities-icons/calendar.svg" alt="calendar" width="15px" style="margin-right: 5px;">
                        <p><b>Last date</b>: ${obj.lastDate}</p>
                    </div>
                </div>
                <div class="sal-last">
                    <div class="sal">
                        <img src="https://caddcentre.com/assets/images/placement/opportunities-icons/job.svg" alt="salary" width="15px" style="margin-right: 5px;">
                        <p><b>Category</b>: ${obj.category}</p>
                    </div>
                    <div class="last">
                        <img src="https://caddcentre.com/assets/images/placement/opportunities-icons/duration.svg" alt="calendar" width="15px" style="margin-right: 5px;">
                        <p><b>Duration</b>: Permanent</p>
                    </div>
                </div>
                <div class="loc">
                    <img src="	https://caddcentre.com/assets/images/placement/opportunities-icons/education.svg" width="15px" style="margin-right: 5px;" alt="map">
                    <p><b>Education</b>: ${obj.education}</p>
                </div>
                <div class="loc">
                    <img src="	https://caddcentre.com/assets/images/placement/opportunities-icons/key-requirements.svg" width="14px" style="margin-right: 5px;" alt="map">
                    <p><b>Key requirements</b>:<br>${obj.keyFeatures}<span style="color:#e31e24;">Know more...</span></p>
                </div>
            </div>`);
            })
            jsonTotal.text(response['totalLength']);
        },
    });
}

categorySearch.change(()=>{
    filterPlacementObjects();
});

departmentSearch.change(()=>{
    filterPlacementObjects();
});

locationSearch.change(()=>{
    filterPlacementObjects();
});

loadMoreButton.on('click', ()=>{
    loadMoreObjects();
});