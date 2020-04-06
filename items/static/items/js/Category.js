window.onload = () => {
    const products = document.getElementsByClassName('products-container');
    
    for (const product of products) {
        product.addEventListener('click', function() {
            const slug = product.querySelector('#product-url').value;
            window.location.href = `${slug}/`;
        });
        const productStock =product.querySelector('#product-stock').value;
        console.log(productStock)
        
                if(productStock < 1){
                    const stock = product.querySelector('#stock');
                    stock.innerHTML = "Nie je skladom";
                    stock.style.color = "#ff0f0f";
                } 

    }
}
    
