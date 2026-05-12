const sizeButtons = document.querySelectorAll(".size-btn");
const sizeInput = document.getElementById("selected-size");

sizeButtons.forEach(button => {

    button.addEventListener("click", function () {

        // remove selected from all
        sizeButtons.forEach(btn => {
            btn.classList.remove("selected");
        });

        // add selected
        this.classList.add("selected");

        // hidden input value
        sizeInput.value = this.dataset.size;

    });

});

function changeImage(element) {
    document.getElementById("mainImage").src = element.src;
}