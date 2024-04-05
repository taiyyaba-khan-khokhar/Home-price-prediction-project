function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for(var i in uiBHK) {
    if(uiBHK[i].checked) {
        return parseInt(uiBHK[i].value); // Use value instead of index
    }
  }
  return -1; // Invalid Value
}

function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(uiBathrooms[i].value); // Use value instead of index
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("uiSqft").value;
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations").value;
  var estPrice = document.getElementById("uiEstimatedPrice");

  console.log("Sqft:", sqft);
  console.log("BHK:", bhk);
  console.log("Bathrooms:", bathrooms);
  console.log("Location:", location);

 // var url = "http://127.0.0.1:8000/api/predict_home_price";
  var url = "/api/predict_home_price";
  $.ajax({
    type: "POST",
    url: url,
    contentType: "application/json",
    data: JSON.stringify({
      total_sqft: parseFloat(sqft),
      bhk: bhk,
      bath: bathrooms,
      location: location
    }),
    success: function(data, status) {
      console.log("Response Data:", data);
      console.log("Status:", status);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
    },
    error: function(xhr, status, error) {
      console.error("Error:", error);
      // Handle error here, e.g., display error message to the user
    }
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  //var url = "http://127.0.0.1:8000/api/get_location_names";
  var url = "/api/get_location_names";
  $.get(url, function(data, status) {
      console.log("got response for get_location_names request");
      console.log("Data:", data);
      console.log("Status:", status);
      if(data && data.locations) {
          var locations = data.locations;
          console.log("Locations:", locations);

          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
}

$(document).ready(function() {
  onPageLoad();
  $('#estimatePriceButton').click(onClickedEstimatePrice);
});


