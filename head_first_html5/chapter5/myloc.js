window.onload = getMylocation;

function getMylocation(){
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(displayLocation);
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