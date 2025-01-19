document.getElementById("review-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const url = document.getElementById("url").value;
    const response = await fetch(/api/reviews?page=${encodeURIComponent(url)});
    const data = await response.json();

    const container = document.getElementById("reviews-container");
    container.innerHTML = JSON.stringify(data, null, 2);
});
