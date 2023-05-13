var slidePosition = 1;
var timeoutId = setTimeout(SlideTimer, 5000);

SlideShow(slidePosition);

// forward/Back controls
function plusSlides(n) {
    SlideShow(slidePosition += n);
}

//  images controls
function currentSlide(n) {
    SlideShow(slidePosition = n);
}

function SlideShow(n) {
    clearTimeout(timeoutId)
    var i;
    var slides = document.getElementsByClassName("container");
    var circles = document.getElementsByClassName("dots");
    if (n > slides.length) {slidePosition = 1}
    if (n < 1) {slidePosition = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
        circles[i].className = circles[i].className.replace(" enable", "");
    }
    if (slidePosition > slides.length) {
        slidePosition = 1
    }
    
    slides[slidePosition-1].style.display = "block";
    circles[slidePosition-1].className += " enable";
    console.log(slidePosition);
    timeoutId = setTimeout(SlideTimer, 5000);
} 



function SlideTimer() {
    slidePosition++;
    SlideShow(slidePosition);
}