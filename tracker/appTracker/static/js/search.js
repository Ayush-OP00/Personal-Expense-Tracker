document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("searchExpense");

    if (!searchInput) return;

    const rows = document.querySelectorAll(".expense-table tbody tr");

    const noResults = document.getElementById("noResults");

    searchInput.addEventListener("keyup", function () {

        let visible = 0;

        rows.forEach(row => {

            const text = row.innerText.toLowerCase();

            if (text.includes(value)) {

                row.style.display = "";

                visible++;

            } else {

                row.style.display = "none";

            }

        });

        if (noResults) {

    if (visible === 0) {

        noResults.classList.remove("d-none");

    } else {

        noResults.classList.add("d-none");

    }

}

        const value = this.value.toLowerCase().trim();

        rows.forEach(row => {

            const text = row.innerText.toLowerCase();

            if (text.includes(value)) {

                row.style.display = "";

            } else {

                row.style.display = "none";

            }

        });

    });

});