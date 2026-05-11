document.addEventListener("DOMContentLoaded", function () {
    let selectedSize = null;

    document.querySelectorAll('.size-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            document.querySelectorAll('.size-btn')
                .forEach(b => b.classList.remove('active'));

            this.classList.add('active');
            selectedSize = this.getAttribute('data-id');

            console.log("Selected Size:", selectedSize);
        });
    });
});



