// Functional Scripts for Python Bottle Application
// Written by Joe Stanley - Stanley Solutions

// Define standard alert function
function msg(alert_string){
    alert( alert_string );
}

// Define standard prompt to load html function
function input_to_html(html_id, prompt_string, default_string='',
                       pre_html='', post_html=''){
    // Capture User Input
    var userinput = prompt(prompt_string, default_string);
    if (userinput != null){
        // Set Inner HTML with User Input and Pre/Post HTML
        document.getElementById( html_id ).innerHTML = 
        pre_html + userinput + post_html;
    }
}

// Define standard prompt to load html attribute function
function input_to_attribute(html_id, prompt_string, default_string='',
                            attribute='value', pre_html='', post_html=''){
    // Capture User Input
    var userinput = prompt(prompt_string, default_string);
    if (userinput != null){
        // Set Inner HTML with User Input and Pre/Post HTML
        document.getElementById( html_id ).setAttribute(attribute, 
                                           pre_html+userinput+post_html);
    }
}

// Define standard prompt to redirect function
function input_to_redirect(prompt_string, default_string='',
                           pre_uri='', post_uri='',domain=null){
    // Capture User Input
    var userinput = prompt(prompt_string, default_string);
    if (userinput != null){
        // Capture Domain if Needed
        if (domain == null){
            var arr = window.location.href.split("/");
            domain = arr[0] + "//" + arr[2];
        }
        // Construct URL to Redirect to
        var url = '';
        // pre_uri is present, use it
        if (pre_uri != ''){
        	url = domain + '/' + pre_uri + '/' + userinput;
        }
        // pre_uri is not present
        else{
        	url = domain + '/' + userinput;
        }
        // If post_uri present, use it
        if (post_uri != ''){
        	url = url + '/' + post_uri
        }
        // Redirect
        location.replace(url)
    }
}

// Define standard confirmation prompt function
function confirm_to_redirect(prompt_string, uri='', domain=null){
    // Confirm redirect with user
    var userinput = confirm(prompt_string);
    if (userinput == true){
        // Capture Domain if Needed
        if (domain == null){
            var arr = window.location.href.split("/");
            domain = arr[0] + "//" + arr[2];
        }
        // Construct URL to Redirect to
        var url = '';
        url = domain + '/' + uri;
        // Redirect
        location.replace(url);
    }
}

// Define Internal Countdown Redirect
function decrement_redirect(id, uri='', domain=null){
    var i = document.getElementById(id);
    // Redirect When Timer Expires
    if (parseInt(i.innerHTML)<=0) {
        // Capture Domain if Needed
        if (domain == null){
            var arr = window.location.href.split("/");
            domain = arr[0] + "//" + arr[2];
        }
        // Construct URL to Redirect to
        var url = '';
        url = domain + '/' + uri;
        // Redirect
        location.replace(url);
    }
    // Count Down
    if (parseInt(i.innerHTML)!=0) {
        i.innerHTML = parseInt(i.innerHTML)-1;
    }
}
// Define Countdown Redirect Call
function countdown_redirect(id, uri='', domain=null){
    // Set Interval
    setInterval(function(){decrement_redirect(id, uri, domain);},1000);
}

// END