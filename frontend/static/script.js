function previewImage() {
    var fileInput = document.getElementById('fileToUpload');
    var file = fileInput.files[0];
    var reader = new FileReader();

    reader.onload = function(e) {
        var thumbnail = document.getElementById('thumbnail');
        thumbnail.src = e.target.result;
    }

    reader.readAsDataURL(file);
}

function uploadImage() {
    var loader = document.querySelector(".loader");
    var thumbnail = document.getElementById("thumbnail");
    var uploadContainer = document.querySelector(".upload-container");
    var paragraphElement = uploadContainer.querySelector("p");
    
    thumbnail.style.opacity = "25%";
    loader.style.display = "block";
    paragraphElement.style.display = "none";
}

