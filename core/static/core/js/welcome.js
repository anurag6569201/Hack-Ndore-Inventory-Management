const progressCircle = document.querySelector(".autoplay-progress svg");
const progressContent = document.querySelector(".autoplay-progress span");
var swiper = new Swiper(".mySwiper", {
    spaceBetween: 30,
    centeredSlides: true,
    loop:true,
    autoplay: {
        delay: 2500, slidesPerView: 1,
        disableOnInteraction: false
    },
    pagination: {
        el: ".mySwiper-swiper-pagination",
        clickable: true
    },
    navigation: {
        nextEl: ".mySwiper-swiper-button-next",
        prevEl: ".mySwiper-swiper-button-prev"
    },
    on: {
        autoplayTimeLeft(s, time, progress) {
            progressCircle.style.setProperty("--progress", 1 - progress);
            progressContent.textContent = `${Math.ceil(time / 1000)}s`;
        }
    }
});
