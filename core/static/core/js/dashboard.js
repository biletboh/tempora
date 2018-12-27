$(function () {
  // change trash icon for ajax selects
  function prettifyKillicon() {
    var kill = $('.ui-icon.ui-icon-trash');
    kill.empty();
    kill.append('<i class="fa fa-lg fa-trash" aria-hidden="true"></i>');
    console.log(kill);
  };

  prettifyKillicon();
});

// Validation
function setFormValidation(id){
  $(id).validate({
    lang: 'uk',
    errorPlacement: function(error, element) {
      $(element).parent('div').addClass('has-error');
      if (element.is(':checkbox')) {
        error.insertAfter(element.parent());}
      else {
        error.insertAfter(element);
      }
    },
  });
};
