window.onload = () => {

var productStock = document.getElementById('product-stock').value;
    if(productStock < 1){
        var stock = document.getElementById('stock');
        stock.innerHTML = "Nie je skladom";
        stock.style.color = "#ff0f0f";
    }
}
