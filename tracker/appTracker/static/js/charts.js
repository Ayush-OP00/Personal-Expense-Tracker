console.log("charts.js loaded");
document.addEventListener("DOMContentLoaded", () => {

    const monthly = JSON.parse(
        document.getElementById("monthly-data").textContent
    );
    console.log(monthly);

    const category = JSON.parse(
        document.getElementById("category-data").textContent
    );
    console.log(category);

    // ---------- Monthly Chart ----------

    new Chart(

        document.getElementById("monthlyChart"),

        {

            type: "line",

            data: {

                

                labels: monthly.map(item => item.month),

                

                datasets: [{

                    label: "Monthly Expense",

                    data: monthly.map(item => item.total),

                    borderWidth: 3,

                    tension: .4,

                    fill: true,

                    pointRadius: 6,

                    pointHoverRadius: 8,

                    borderColor: "#3B82F6",

                    backgroundColor: "rgba(59,130,246,.2)",

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio:false,

                plugins:{

                    legend:{

                        display:false

                    }

                }

            }

        }

    );



    // ---------- Doughnut Chart ----------

    new Chart(

    document.getElementById("categoryChart"),

    {

        type: "doughnut",

        data: {

            labels: category.map(item => item.category),

            datasets: [{

                label: "Expenses",

                data: category.map(item => item.total),

                backgroundColor: [

                    "#3B82F6",

                    "#10B981",

                    "#F59E0B",

                    "#EF4444",

                    "#8B5CF6"

                ],

                borderWidth: 1

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    position: "bottom"

                }

            }

        }

    }

);

});