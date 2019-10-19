window.onload = getMylocation;

function getMylocation(){
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(displayLocation,displayError);
    }else{
        alert("Oops , no geolocation support");
    }
}

function displayLocation(position){
    alert('cheng')
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    var div = document.getElementById("location");
    div.innerHTML = "You are at Latitude:"+latitude+",longitude:"+longitude;
}

function displayError(error){
    var errorTypes ={
        0:"Unknown error",
        1:"Permission denied by user",
        2:"Position is not available",
        3:"Request timed out"
    };
    var errorMessage = errorTypes[error.code];
    if (error.code == 0 || error.code ==2){
        errorMessage = errorMessage +" "+errorMessage;

    }
    var div = document.getElementById("location");
    div.innerHTML = errorMessage;
}: