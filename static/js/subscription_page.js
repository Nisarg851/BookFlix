const freeBtn = document.getElementById('free-btn');
const goldBtn = document.getElementById('gold-btn');
const platinumBtn = document.getElementById('platinum-btn');

freeBtn.addEventListener('click', () => {
    console.log("Clicked on Free button");
    window.location.href = 'payment_page.html';
});

goldBtn.addEventListener('click', () => {
    window.location.href = 'payment_page.html';
});

platinumBtn.addEventListener('click', () => {
    window.location.href = 'payment_page.html';
});

