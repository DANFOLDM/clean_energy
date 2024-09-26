// Modal Functionality
const modal = document.getElementById('product-modal');
const modalImg = document.getElementById('modal-img');
const modalTitle = document.getElementById('modal-title');
const modalPrice = document.getElementById('modal-price');
const closeModalBtn = document.querySelector('.close-btn');
const viewDetailsBtns = document.querySelectorAll('.view-details-btn');

viewDetailsBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        const productCard = this.parentElement;
        const imgSrc = productCard.querySelector('img').src;
        const title = productCard.querySelector('h3').textContent;
        const price = productCard.querySelector('p').textContent;

        modalImg.src = imgSrc;
        modalTitle.textContent = title;
        modalPrice.textContent = price;
        modal.style.display = 'flex';
    });
});

closeModalBtn.addEventListener('click', () => {
    modal.style.display = 'none';
});

// Filter Functionality
const categoryNavItems = document.querySelectorAll('.category-nav ul li');
const productCards = document.querySelectorAll('.product-card');

categoryNavItems.forEach(item => {
    item.addEventListener('click', function() {
        const category = this.getAttribute('data-category');

        productCards.forEach(card => {
            const cardCategory = card.getAttribute('data-category');
            if (category === 'all' || cardCategory === category) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });

        categoryNavItems.forEach(navItem => navItem.classList.remove('active'));
        this.classList.add('active');
    });
});

// button 
const buyNowBtn = document.querySelector('.buy-now-btn');

buyNowBtn.addEventListener('click', () => {
    const productTitle = document.getElementById('modal-title').textContent;
    alert(`You selected to buy: ${productTitle}`);
    // You can add more functionality like redirecting to a checkout page
});

// shopping button 
function goToNewPage() {
    window.location.href = 'file:///C:/Users/USER/Desktop/ECO-VENTURES/paypage.html'; // Replace with your desired URL
}