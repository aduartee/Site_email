window.addEventListener("load", function() {
    setTimeout(function() {
      document.getElementById("preloader").style.opacity = "0";
    }, 500);
  });
  
  document.getElementById("preloader").addEventListener("transitionend", function() {
    this.style.display = "none";
  });