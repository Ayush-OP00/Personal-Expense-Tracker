document.addEventListener("DOMContentLoaded", function () {

    const toastElements = document.querySelectorAll(".toast");

    toastElements.forEach(function (toastElement) {

        const toast = new bootstrap.Toast(toastElement, {
            delay: 3500,
            autohide: true
        });

        toast.show();

    });

});