function copiarTicket() {
    const texto = document.getElementById("ticket-text").innerText;

    navigator.clipboard.writeText(texto).then(() => {
        const mensaje = document.getElementById("mensaje-copiado");
        mensaje.style.opacity = 1;
        mensaje.style.visibility = "visible";

        setTimeout(() => {
            mensaje.style.opacity = 0;
            mensaje.style.visibility = "hidden";
        }, 2000);
    }).catch(err => {
        console.error("Error al copiar el ticket:", err);
    });
}