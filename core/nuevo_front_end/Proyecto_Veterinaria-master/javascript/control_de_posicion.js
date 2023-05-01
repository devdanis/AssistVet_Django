// Detectar el ancho de la pantalla
const width =
    window.innerWidth ||
    document.documentElement.clientWidth ||
    document.body.clientWidth;

// Aplicar estilos CSS según el ancho de la pantalla
if (width >= 768) {
    document
        .getElementsByClassName("position")
        .classList.add("pantalla-grande");
} else {
    document.getElementById("position").classList.add("pantalla-pequeña");
}
