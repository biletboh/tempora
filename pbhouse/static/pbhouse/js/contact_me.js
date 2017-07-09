$(function() {
  // Submit form
  $('#contactForm').on('submit', function(event){
    event.preventDefault();
    send_message();
  });

  // Ajax for posting 
  function send_message() {
    var name = $('#id_name').val();
    var email = $('#id_email').val();
    var phone = $('#id_phone').val();
    var message = $('#id_message').val();

    var formData = new FormData();
    
    formData.append('name', name);
    formData.append('email', email);
    formData.append('phone', phone);
    formData.append('message', message);

    console.log(formData)
    $.ajax({
      url : window.location.href, // the endpoint
      type : "POST", // http method
      data : formData, // data sent with the post request

      processData: false,  // tell jQuery not to process the data
      contentType: false,

      // handle a successful response
      success : function(json) {
        $('#id_name').val(''); // remove the value from the input
        $('#id_email').val(''); // remove the value from the input
        $('#id_phone').val(''); // remove the value from the input
        $('#id_message').val(''); // remove the value from the input
        $('#message').html("<div class='alert bg-success'>Повідомлення надіслано!"+"<button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>"); // add success message 

      },
      // handle a non-successful response
      //error : function(jqXHR,errmsg,err) {
      error : function(xhr,textStatus,errorThrown) {
          var data = xhr.responseText;
          var jsonResponse = JSON.parse(data);
          jQuery.each(jsonResponse, function(key, value) { 
            $("#message").append("<div class='alert alert-danger'>"+value+"<button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button>");
          });
      }
    });
  };

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
      (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
      // or any other URL that isn't scheme relative or absolute i.e relative.
      !(/^(\/\/|http:|https:).*/.test(url));
  }

    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
        // Send the token to same-origin, relative URLs only.
        // Send the token only if the method warrants CSRF protection
        // Using the CSRFToken value acquired earlier
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });
});

