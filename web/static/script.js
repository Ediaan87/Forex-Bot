// JavaScript code for interactivity and real-time updates

// Add event listener to the button
document.getElementById("override-button").addEventListener("click", function() {
  // Get the input value
  var inputValue = document.getElementById("override-input").value;
  
  // Make a POST request to the server
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/override", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      // Handle the response from the server
      var response = JSON.parse(xhr.responseText);
      if (response.success) {
        alert("Override successful!");
      } else {
        alert("Override failed!");
      }
    }
  };
  xhr.send(JSON.stringify({ value: inputValue }));
});