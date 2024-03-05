const gallery = document.querySelector('.gallery');

const masonry = new Masonry(gallery, {
    itemSelector: '.item',
    percentPosition: true
});

imagesLoaded(gallery).on('progress', function () {
    masonry.layout();
});
