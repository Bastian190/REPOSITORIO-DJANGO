$(document).ready(function () {
    $("#submit").click(function () {
      var name = $("#name").val();
      var email = $("#email").val();
      var pass = $("#password").val();

      if (name.length == "") {
        $("#p1").text("ingresa tu nombre");
        $("#name").focus();
        return false;
      } else if (email.length == "") {
        $("#p2").text("ingresa tu correo");
        $("#email").focus();
        return false;
      } else if (pass.length == "") {
        $("#p3").text("ingresa tu contraseña");
        $("#password").focus();
        return false;
      } 
    });
  });