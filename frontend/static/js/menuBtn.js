let menuBtn = document.querySelector('.header__navigation_menu');
let menuBtnLines = document.querySelector('.header__navigation_menu-lines');
let menu = document.querySelector('.menu');
let header = document.querySelector('.header');
let body = document.querySelector('body');
let menuText = document.querySelector('.header__navigation_menu-description');
let headerList = document.querySelector('.header__navigation_list');
let headerPhone = document.querySelector('.header__navigation_phone');

menuBtn.addEventListener('click', function(){
    menuBtnLines.classList.toggle('active');
    menu.classList.toggle('active');
    header.classList.toggle('active');
    body.classList.toggle('lock');
    (menuText.innerHTML === 'Меню') ? menuText.innerHTML = 'Закрыть' : menuText.innerHTML = 'Меню';
    headerList.classList.toggle('visually-hidden');
    headerPhone.classList.toggle('visually-hidden');
})


