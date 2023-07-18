function validateContactForm(){
    let valueToBeVerified = document.forms['contactForm']['verification'].value;
    let verifiedValue = document.getElementById('verification-id').innerHTML;
    console.log(verifiedValue);
    if(valueToBeVerified != verifiedValue){
        alert("Verification value is wrong!");
        return false;
    }
    
}