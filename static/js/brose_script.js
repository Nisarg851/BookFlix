const slider = document.querySelector(".slider");
const slides = document.querySelectorAll(".slide");
const slideWidth = slides[0].offsetWidth;
const prevBtn = document.querySelector(".prev-btn");
const nextBtn = document.querySelector(".next-btn");

let currentSlide = 0;
let intervalId;

function moveSlides() {
  slider.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
}

function autoSlide() {
  if (currentSlide >= slides.length - 1) {
    currentSlide = 0;
  } else {
    currentSlide++;
  }
  moveSlides();
}

intervalId = setInterval(autoSlide, 3000);

nextBtn.addEventListener("click", () => {
  clearInterval(intervalId);
  if (currentSlide >= slides.length - 1) {
    currentSlide = 0;
  } else {
    currentSlide++;
  }
  moveSlides();
  intervalId = setInterval(autoSlide, 3000);
});

prevBtn.addEventListener("click", () => {
  clearInterval(intervalId);
  if (currentSlide <= 0) {
    currentSlide = slides.length - 1;
  } else {
    currentSlide--;
  }
  moveSlides();
  intervalId = setInterval(autoSlide, 3000);
});
