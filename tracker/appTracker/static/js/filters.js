document.addEventListener("DOMContentLoaded", function () {

    const categoryFilter = document.getElementById("categoryFilter");
    const dateFilter = document.getElementById("dateFilter");
    const resetButton = document.getElementById("resetFilters");
    const searchInput = document.getElementById("searchExpense");
    const noResults = document.getElementById("noResults");
    const rows = document.querySelectorAll(".expense-table tbody tr");

    if (!searchInput) return;


    function applyFilters() {

        const searchValue = searchInput.value.toLowerCase().trim();
        const categoryValue = categoryFilter.value.toLowerCase();
        const dateValue = dateFilter.value;

        let visible = 0;

        // rows.forEach(console.log({
        //     title,
        //     category,
        //     date,
        //     searchValue,
        //     categoryValue,
        //     dateValue,
        //     matchesSearch,
        //     matchesCategory,
        //     matchesDate
        // });)

rows.forEach(row => {

    const title = row.cells[0].innerText.toLowerCase();
    const category = row.cells[1].innerText.toLowerCase();
    const date = row.dataset.date;

    const searchableText =
        `${title} ${category}`.toLowerCase();

    const matchesSearch =
        searchableText.includes(searchValue);

    const matchesCategory =
        !categoryValue || category.includes(categoryValue);

    const matchesDate =
        !dateValue || date === dateValue;

    if (matchesSearch && matchesCategory && matchesDate) {

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

    }

searchInput.addEventListener("input", applyFilters);

categoryFilter.addEventListener("change", applyFilters);

dateFilter.addEventListener("change", applyFilters);

resetButton.addEventListener("click", function () {

    searchInput.value = "";
    categoryFilter.value = "";
    dateFilter.value = "";

    applyFilters();

    searchInput.focus();

});

});