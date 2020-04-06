document.addEventListener("DOMContentLoaded", functionLoaded); 

function functionLoaded(){
    
    document.getElementById("responzivita").addEventListener("click", function() {
        if (document.getElementById("tab").style.display === "block") {
            document.getElementById("tab").style.display = null;
        } else {
            document.getElementById("tab").style.display = "block";
        }
    });
}
    

