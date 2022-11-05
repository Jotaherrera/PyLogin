$('form[name=signup_form').submit(function (e) {
  var $form = $(this);
  var $error = $form.find('.error');
  var data = $form.serialize();

  $.ajax({
    url: '/sign-up',
    type: 'POST',
    data: data,
    dataType: 'json',
    success: function (resp) {
      window.location.href = '/account';
    },
    error: function (resp) {
      $error.text(resp.responseJSON.error).removeClass('error--hidden');
    },
  });

  e.preventDefault();
});

$('form[name=login_form').submit(function (e) {
  var $form = $(this);
  var $error = $form.find('.error');
  var data = $form.serialize();

  $.ajax({
    url: '/log-in',
    type: 'POST',
    data: data,
    dataType: 'json',
    success: function (resp) {
      window.location.href = '/account';
    },
    error: function (resp) {
      $error.text(resp.responseJSON.error).removeClass('error--hidden');
    },
  });

  e.preventDefault();
});
