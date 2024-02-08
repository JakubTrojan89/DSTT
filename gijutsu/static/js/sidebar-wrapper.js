window.addEventListener('DOMContentLoaded', event => {

    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    const sidebarWrapper = document.body.querySelector('#sidebar-wrapper');

    if (sidebarToggle && sidebarWrapper) {
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            sidebarWrapper.classList.toggle('toggled');
        });
    }

    const sidebarLinks = document.querySelectorAll('#sidebar-wrapper .list-group-item');

    sidebarLinks.forEach(link => {
        link.addEventListener('click', event => {
            const isDsttLink = link.textContent.trim() === 'DSTT';
            if (isDsttLink) {
                event.preventDefault();
                sidebarWrapper.classList.toggle('toggled');
            }
        });
    });

});