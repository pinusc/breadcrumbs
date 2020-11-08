<template>
    <div class=text-center>
        <button class="button is-link" v-on:click="queryLocation">Fetch Location from GPS</button>
        <span class="mx-5">or</span>
        <button class="button is-danger" @click="useDummyLocation">use dummy var for testing</button>
    </div>
</template>

<script>
function displayLocation(that, position) { 
    var displayText = "Your latitude is " + position.coords.latitude + " and longitude is " + position.coords.longitude;
    that.$root.$data.vuey.userLocation = {
        "lat": position.coords.latitude,
        "lon": position.coords.longitude
    };
    document.getElementById("locationData").innerHTML = displayText;
}

function displayError(error) { 
    
    //get a reference to the HTML element for writing result
    var locationElement = document.getElementById("locationData");

    //find out which error we have, output message accordingly
    switch(error.code) {
        case error.PERMISSION_DENIED:
            locationElement.innerHTML = "Permission was denied";
            break;
        case error.POSITION_UNAVAILABLE:
            locationElement.innerHTML = "Location data not available";
            break;
        case error.TIMEOUT:
            locationElement.innerHTML = "Location request timeout";
            break;
        case error.UNKNOWN_ERROR:
            locationElement.innerHTML = "An unspecified error occurred";
            break;
        default:
            locationElement.innerHTML = "Who knows what happened...";
            break;
    }}

export default {
    name: 'LocationManager',
    props: {
    },
    methods:{
        queryLocation () { 
            //check if the geolocation object is supported, if so get position
            if (navigator.geolocation)
                navigator.geolocation.getCurrentPosition((pos) => {displayLocation(this, pos);}, displayError);
            else
                document.getElementById("locationData").innerHTML = "Sorry - your browser doesn't support geolocation!";
        },
        useDummyLocation(){
            this.$root.$data.vuey.userLocation = {
                "lat": 51.500944,
                "lon": 0.124618
            };
            console.log("added test lat/lon because lat/lon was not available");
        }

    }
}
</script>

<style scoped>

</style>
