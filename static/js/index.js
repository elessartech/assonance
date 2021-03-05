const menuBtn = document.querySelector("#menu-btn");
const sidebar = document.querySelector("#sidebar");
const mainContainer = document.querySelector("#main-container");

menuBtn.addEventListener("click", () => {
  sidebar.classList.toggle("side-navbar-active");
  menuBtn.classList.toggle("menu-btn-active");
  mainContainer.classList.toggle("main-container-active");
});