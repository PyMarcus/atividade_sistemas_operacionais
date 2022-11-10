
document.getElementById("bt").addEventListener("click", fn);


function fn(){
    setTimeout(function() {
      window.location.reload(1);
    }, 1000);
}


setTimeout(function() {
      window.location.reload(1);
    }, 10000);