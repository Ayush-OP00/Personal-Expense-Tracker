document.addEventListener("DOMContentLoaded", () => {

    function setupToggle(inputId, buttonId) {

        const input = document.getElementById(inputId);
        const button = document.getElementById(buttonId);

        if (!input || !button) return;

        button.addEventListener("click", () => {

            const icon = button.querySelector("i");

            if (input.type === "password") {

                input.type = "text";
                icon.classList.replace("bi-eye", "bi-eye-slash");

            } else {

                input.type = "password";
                icon.classList.replace("bi-eye-slash", "bi-eye");

            }

        });

    }

    setupToggle("password", "togglePassword");
    setupToggle("confirmPassword", "toggleConfirmPassword");

});