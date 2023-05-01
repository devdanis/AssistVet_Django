const galleryImages = document.querySelectorAll(".gallery");
const galleryContainerSelect = document.querySelector(
    ".cat_img-focus_container"
);
const imageContainer = document.querySelector(".cat_img-focus_img");
const leyenda = document.querySelector(".cat_img-focus_leyenda");
const cerrar = document.querySelector(".cat_img-focus_bx-x");

galleryImages.forEach((image) => {
    image.addEventListener("click", () => {
        addImage(image.getAttribute("src"), image.getAttribute("alt"));
    });
});

const addImage = (srcImage, altImage) => {
    galleryContainerSelect.classList.toggle("move");
    imageContainer.src = srcImage;
    leyenda.innerHTML = altImage;
};

//  galleryContainerSelect.addEventListener('click', ()=>{
//    galleryContainerSelect.classList.toggle('move')

//  });

cerrar.addEventListener("click", () => {
    galleryContainerSelect.classList.toggle("move");
});
