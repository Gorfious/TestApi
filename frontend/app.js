const API_URL = "/api/customers";

async function loadCustomers() {

    const response = await fetch(API_URL);

    const customers = await response.json();

    const list = document.getElementById("customerList");

    list.innerHTML = "";

    customers.forEach(customer => {

        const li = document.createElement("li");

        li.textContent =
            `${customer.id} - ${customer.name}`;

        list.appendChild(li);
    });
}

async function addCustomer() {

    const name =
        document.getElementById("name").value;

    await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name
        })
    });

    document.getElementById("name").value = "";

    loadCustomers();
}

loadCustomers();

fetch("/api/customers")