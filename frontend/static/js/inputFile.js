var outputfileName = document.getElementById("fileName");
var info__file = document.querySelector(".info__file");

document.getElementById('file').onchange = function () {
    outputfileName.innerHTML = this.files.item(0).name;
    info__file.classList.add('fileYes');
};