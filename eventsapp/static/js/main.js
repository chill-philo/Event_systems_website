document.addEventListener("DOMContentLoaded", function () {
    const productLinks = document.querySelectorAll(".service a");

    productLinks.forEach(link => {
        link.addEventListener("click", function (event) {
            console.log("Clicked link ID:", this.id);
        });
    });
});