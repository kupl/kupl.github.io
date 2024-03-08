// Enable lazy loading for image thumbnails
document.addEventListener("DOMContentLoaded", function () {
    const lazyloadImages = document.querySelectorAll(".lazy");
    const imageObserver = new IntersectionObserver(function (entries, observer) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                const image = entry.target;
                image.src = image.dataset.src;
                image.classList.remove("lazy");
                imageObserver.unobserve(image);
            }
        });
    });

    lazyloadImages.forEach(function (image) {
        imageObserver.observe(image);
    });

});

// Build masonry layout one by one
const galleryHolders = document.querySelectorAll('.gallery-holder');
galleryHolders.forEach((galleryHolder) => {
    const target = document.querySelector(galleryHolder.dataset.galleryTarget);
    const masonry = new Masonry(target, {
        itemSelector: '.gallery-item',
        percentPosition: true,
        transitionDuration: 0,
    });

    const nItems = galleryHolder.children.length;
    for (let i = 0; i < nItems; i++) {
        const item = galleryHolder.children[0];
        target.appendChild(item);
        masonry.appended([item]);
        masonry.layout();
    }

    galleryHolder.remove();
});
