const nav_menu = document.getElementById("nav__menu");
const nav_menu_alimentos = document.getElementById(
    "nav__menu_submenu-alimentos"
);
const nav_menu_servicios = document.getElementById(
    "nav__menu_submenu-servicios"
);

function menu() {
    if (nav_menu.style.display === "block") {
        nav_menu.style.display = "none";
        nav_menu_alimentos.style.display = "none";
        nav_menu_servicios.style.display = "none";
    } else {
        nav_menu.style.display = "block";
        nav_menu.style.position = "absolute";
        nav_menu_alimentos.style.display = "none";
        nav_menu_servicios.style.display = "none";
    }
}

function submenuAlimentos() {
    if (nav_menu_alimentos.style.display === "block") {
        nav_menu_alimentos.style.display = "none";
        nav_menu_servicios.style.display = "none";
    } else {
        nav_menu_alimentos.style.display = "block";
        nav_menu_alimentos.style.position = "absolute";
        nav_menu_servicios.style.display = "none";
    }
}

function submenuServicios() {
    if (nav_menu_servicios.style.display === "block") {
        nav_menu_servicios.style.display = "none";
        nav_menu_alimentos.style.display = "none";
    } else {
        nav_menu_servicios.style.display = "block";
        nav_menu_servicios.style.position = "absolute";
        nav_menu_alimentos.style.display = "none";
    }
}

//   function prod() {
//     var x = document.getElementById("nav__prod");
//     console.log(x);
//     if (x.style.display === "block") {
//       x.style.display = "none";
//     }
//     else {
//       x.style.display = "block";
//       x.style.position = "absolute";
//     }
//   }

const btnProductos = document.querySelector("#productos");
// const btnProductos = document.getElementById('productos');
const menuProductos = document.querySelector(".nav__prod");
const menuServicios = document.querySelector(".nav__serv");
const btnServicios = document.querySelector("#servicios");
const tocarBody = document.getElementsByTagName("body")[0];
const tocarVideo = document.querySelectorAll(".videos");

btnProductos.addEventListener("mouseover", () => {
    menuServicios.style.display = "none";
    menuProductos.style.display = "block";
    menuProductos.style.position = "absolute";
});

menuServicios.addEventListener("mouseover", () => {
    menuServicios.style.display = "block";
    menuServicios.style.position = "absolute";
});

menuProductos.addEventListener("mouseleave", () => {
    menuProductos.style.display = "none";
});

menuServicios.addEventListener("mouseleave", () => {
    menuServicios.style.display = "none";
});

btnServicios.addEventListener("mouseover", () => {
    menuProductos.style.display = "none";
    menuServicios.style.display = "block";
    menuServicios.style.position = "absolute";
    // menuProductos.style.position = "absolute";
});

tocarBody.addEventListener("click", () => {
    menuProductos.style.display = "none";
    menuServicios.style.display = "none";
});

tocarVideo.forEach((video) => {
    video.addEventListener("click", () => {
        menuProductos.style.display = "none";
    });
});
