var menu = document.getElementById("float-menu");
open = document.getElementById("float-open");
close = document.getElementById("float-close");
open.addEventListener("click", function () {
  menu.classList.toggle("active");
  open.classList.toggle("hide");
});
