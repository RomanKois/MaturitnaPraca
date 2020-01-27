window.onload = () => {
    const products = document.getElementsByClassName('products-container');
    
    for (const product of products) {
        product.addEventListener('click', function() {
            const slug = product.querySelector('#product-url').value;
            window.location.href = `${slug}/`;
        });
    }
}
    
