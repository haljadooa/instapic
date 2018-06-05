$(document).ready(function() {
    // once the "Go" button is clicked
    // download process will start
   $('#go').on('click', function() {

       // url provided by the user
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
                        
                        let content_url = response.data.data.url,
                            content_type = response.data.data.type
                        
                        // check if the returned content is a photo or a video
                        if(content_type == "image") {
                            // set the elements attrs with the proper URLs
                            $("#image").attr("src", content_url)
                            $("#image-download").attr("href", content_url + "?dl=1")
        
                            // display preview window
                            $("#image-preview").modal('show')
                        }  
                        else if (content_type == "video") {
                            // set the elements attrs with the proper URLs
                            $("#video").attr("src", content_url)
                            $("#video-download").attr("href", content_url + "?dl=1")
        
                            // display preview window
                            $("#video-preview").modal('show')
                        }    
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