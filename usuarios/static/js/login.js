// Mostrar/Ocultar contraseña
function togglePassword() {
    const input = document.getElementById("id_password");
    input.type = input.type === "password" ? "text" : "password";
}

// Validación simple antes de enviar
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    form.addEventListener("submit", function (e) {
        const username = document.getElementById("id_username").value.trim();
        const password = document.getElementById("id_password").value.trim();

        if (!username || !password) {
            alert("Por favor completa todos los campos.");
            e.preventDefault();
        }
    });
});
