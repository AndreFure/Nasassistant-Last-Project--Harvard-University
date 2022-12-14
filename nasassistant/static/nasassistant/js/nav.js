let toggleImg = document.getElementById('toggleImg');
let imgMenu = document.getElementById('imgMenu');
let headerList = document.getElementById('headerList');
let navbar = document.getElementById('navbar');
let nav1 = document.getElementById('nav1');
let logo = document.getElementById('logo');
let navMenuUl = document.getElementById('navMenuUl');

toggleImg.addEventListener("click", () => {
  toggleImg.classList.toggle("active");
  headerList.classList.toggle("active");
  navbar.classList.toggle("active");
  nav1.classList.toggle("active");
  logo.classList.toggle("active");
  navMenuUl.classList.toggle("active");
})


