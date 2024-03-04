const gallery = document.querySelector('.gallery');

const masonry = new Masonry(gallery, {
    itemSelector: '.item',
    percentPosition: true
});

imagesLoaded(gallery).on('progress', function () {
    masonry.layout();
});

const modals = document.getElementsByClassName('modal');
for(let i = 0; i < modals.length; i++) {
    const modal = modals[i];
    modal.addEventListener('show.bs.modal', event => {
        const recipient = event.relatedTarget.getAttribute('data-bs-image');
        const imgPlaceholder = modal.querySelector('.modal-content img');
        imgPlaceholder.src = recipient;
    });
}
