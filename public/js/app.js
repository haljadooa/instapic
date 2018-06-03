$(document).ready(function() {
    // once the "Go" button is clicked
    // download process will start
   $('#go').on('click', function() {
       let url = document.getElementById('link').value

       // check if a url has been provided
        if(url.length > 1) {
            // check if the url is valid
            if(validateURL(url)){
                /**
                 * Ask the server to retrieve the image link
                 * Once the server has the link it'll send it back
                 */
                axios.post('/download?url=' + url).then(function(response) {
                    // check if the request was successful
                    if(response.status == 200) {
                        // crown jewel
                        let imgUrl = response.data
    
                        // set the elements attrs with the proper URLs
                        $("#image").attr("src", imgUrl)
                        $("#download").attr("href", imgUrl + "?dl=1")
    
                        // display preview window
                        $("#image-preview").modal('show')
                    } else {
                        alert('An unknown error occured');
                    }
                }).catch(function(error) {
                    // print errors in the request to the console
                    console.error(error);
                });
            }
            
        } else {
            alert("No Link Provided")
        }
   });
});

// validate url
// regex courtesy of @franciskim
function validateURL(value) {
    let expression = /[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi
    let regex = new RegExp(expression);
    if(!regex.test(value)) {
        alert('Please enter a valid URL!');
        return false;
    }else {
        return true;
    }
  }