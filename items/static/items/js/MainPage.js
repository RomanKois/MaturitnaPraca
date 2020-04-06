window.onload = () => {    
    const products = document.getElementsByClassName('products-container');    
    
    for (const product of products) {

        const productStock =product.querySelector('#product-stock').value;
        console.log(productStock)
        
                if(productStock < 1){
                    const stock = product.querySelector('#stock');
                    stock.innerHTML = "Nie je skladom";
                    stock.style.color = "#ff0f0f";
                } 

        product.addEventListener('click', function() {
            const category = product.querySelector('#category-url').value;
            const slug = product.querySelector('#product-url').value;
            window.location.href = `category/${category}/${slug}/`;
        });
    }
}
