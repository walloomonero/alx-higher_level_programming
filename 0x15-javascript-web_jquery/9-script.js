// The script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello.

let url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data){
      $("div#hello").text(data.hello);
});
