const menuBtn = document.querySelector("#menu-btn");
const sidebar = document.querySelector("#sidebar");
const mainContainer = document.querySelector("#main-container");
 
const successAlert = document.querySelector("#success-alert");

menuBtn.addEventListener("click", () => {
  sidebar.classList.toggle("side-navbar-active");
  menuBtn.classList.toggle("menu-btn-active");
  mainContainer.classList.toggle("main-container-active");
});

if (successAlert) {
  successAlert.addEventListener("click", () => {
    successAlert.style.opacity = 0;
    setInterval(() => {
      successAlert.style.display = "none";
    }, 600)
  });

  setInterval(() => {
    successAlert.style.opacity = 0;
  }, 4000)

  setInterval(() => {
    successAlert.style.display = "none";
  }, 5000)
}