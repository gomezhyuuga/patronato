// JavaScript Document

$(document).ready(function(){
  $ (".cerrar").click(function(){
    $("#forma").slideUp(500);
  });
  $ (".abrir").click(function(){
    $("#forma").slideDown(2000);
  });
});