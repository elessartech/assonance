var menu_btn = document.querySelector("#menu-btn");
var sidebar = document.querySelector("#sidebar");
var container = document.querySelector("#main-container");
menu_btn.addEventListener("click", () => {
  sidebar.classList.toggle("side-navbar-active");
  menu_btn.classList.toggle("menu-btn-active");
  container.classList.toggle("main-container-active");
});