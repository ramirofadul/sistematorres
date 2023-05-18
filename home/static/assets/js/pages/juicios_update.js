$(function () {

    $(".js-movimientos-create").click(function () {
      $.ajax({
        url: '/juicios/movimientos/create/',
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-juicios").modal("show");
        },
        success: function (data) {
          $("#modal-juicios .modal-body").html(data.html_form);
        }
      });
    });
  
  });
