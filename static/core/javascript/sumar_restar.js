// Obtener todas las referencias a los elementos HTML
const contadores = document.querySelectorAll(".contador");
const botonesSumar = document.querySelectorAll(".btn-sumar");
const botonesRestar = document.querySelectorAll(".btn-restar");

// Asociar eventos a los botones
botonesSumar.forEach((boton, index) => {
    boton.addEventListener("click", () => {
        sumarUno(index);
    });
});

botonesRestar.forEach((boton, index) => {
    boton.addEventListener("click", () => {
        restarUno(index);
    });
});

// Función para sumar uno al contador correspondiente
function sumarUno(index) {
    let contador = parseInt(contadores[index].textContent);
    //contador += 1;
    //contadores[index].textContent = contador;
    if (contador >= 0) {
        contador += 1;
        contadores[index].textContent = contador;
    }
}

// Función para restar uno al contador correspondiente
function restarUno(index) {
    let contador = parseInt(contadores[index].textContent);
    if (contador > 0) {
        contador -= 1;
        contadores[index].textContent = contador;
    }
}
