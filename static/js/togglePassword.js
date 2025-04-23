function togglePasswordVisibility(inputId, buttonId) {
    const passwordField = document.getElementById(inputId);
    const toggleButton = document.getElementById(buttonId);
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        toggleButton.textContent = 'Ocultar';
    } else {
        passwordField.type = 'password';
        toggleButton.textContent = 'Mostrar';
    }
}