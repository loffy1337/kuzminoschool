document.addEventListener('DOMContentLoaded', function() {
    //Кнопка для открытия меню
    let menu_btn = document.querySelector('#header-menu');
    //Кнопка для закрытия меню
    let menu_cross = document.querySelector('#menu-cross');
    //Кнопка "Связаться с нами"
    let btn_contacts = document.querySelector('#btn-contacts');

    menu_btn.addEventListener('click', function() {
        let menu = document.querySelector('#menu');
        menu.classList.add('menu-open');
        document.body.style.position = 'fixed';
    });

    menu_cross.addEventListener('click', function() {
        let menu = document.querySelector('#menu');
        menu.classList.remove('menu-open');
        document.body.style.position = '';
    });

    btn_contacts.addEventListener('click', function() {
        let section_contacts = document.querySelector('#section-contacts');
        section_contacts.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });
});