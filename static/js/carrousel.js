const prev = document.querySelector('.prev');
const next = document.querySelector('.next');
const slides = document.querySelectorAll('.container-elem');
const slideList = document.querySelector('.container-list')
const slideWidth = slides[0].getBoundingClientRect().width;

// arrange the slides next to one another

const setSlidePosition = (slide, index) =>{
    slide.style.left = slideWidth * index + 'px'
}
slides.forEach(setSlidePosition);
   
const moveToSlide = (slideList,currentSlide,targetSlide) => {
    slideList.style.transform = 'translateX(-' + targetSlide.style.left + ')';
    currentSlide.classList.remove('current-elem');
    targetSlide.classList.add('current-elem');
}
// click right button
next.addEventListener('click', (e) =>{
    const currentSlide = slideList.querySelector('.current-elem')
    const nextSlide = currentSlide.nextElementSibling;
    
    // move to the next slide
    moveToSlide(slideList,currentSlide, nextSlide);
});

//click the left button
prev.addEventListener('click', () => {
    const currentSlide = slideList.querySelector('.current-elem')
    const prevSlide = currentSlide.previousElementSibling;
    moveToSlide(slideList,currentSlide ,prevSlide);
});


