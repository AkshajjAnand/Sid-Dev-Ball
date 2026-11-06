async function getRandom() {
    try {
        const response = await fetch("/api/v1/random");
        if (!response.ok) {
            throw new Error("Server replied with status " + response.status);
        }
        const data = await response.json();
        document.getElementById("output").textContent =
            JSON.stringify(data, null, 2);
    } catch (err) {
        document.getElementById("output").textContent = "Error: " + err.message;
    }
}

getRandom();