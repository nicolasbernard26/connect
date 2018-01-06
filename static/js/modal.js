function openModal(src, text){
    var modal = document.getElementById('myModal');
    var modalImg = document.getElementById("img01");
    var captionText = document.getElementById("caption");
    modal.style.display = "block";
    modalImg.src = src;
    captionText.innerHTML = text;
}


// When the user clicks on <span> (x), close the modal
function closeModal() { 
    
// Get the <span> element that closes the modal
    var modal = document.getElementById('myModal');
    modal.style.display = "none";
}