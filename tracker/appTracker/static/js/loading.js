document.addEventListener("DOMContentLoaded", () => {

    const forms = document.querySelectorAll("form");

    forms.forEach(form => {

        form.addEventListener("submit", () => {

            const submitButton = form.querySelector(
                'button[type="submit"]'
            );

            if (!submitButton) return;

            submitButton.disabled = true;

            submitButton.dataset.originalText =
                submitButton.innerHTML;

            submitButton.innerHTML = `
                <span class="spinner-border spinner-border-sm me-2"></span>
                Processing...
            `;

        });

    });

});