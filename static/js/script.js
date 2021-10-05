const open = document.querySelector('.open');
const navbar = document.querySelector('.navigation-list');
const close = document.querySelector('.close');
const navElem = document.querySelectorAll('.navigation-list a li');
const header = document.querySelector('header');
open.addEventListener('click', () => {
    navbar.style.top = "0";
});

close.addEventListener('click', () => {
    navbar.style.top ="-1310%";
});
navElem.forEach((elem) => {
    elem.addEventListener('click', () => {
        navbar.style.top ="-1310%";
    })
})

if(window.pageYOffset >= 1 ){
    header.style.position = "sticky";
    header.style.top = "0";
    header.style.left = "0";
}