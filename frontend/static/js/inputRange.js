var slider = document.getElementById("myRange");
var output = document.getElementById("myValue");


output.innerHTML = slider.value;
slider.oninput = function() {
    output.innerHTML = this.value;
}

slider.addEventListener("mousemove", function() {
    var x = slider.value;
    var color = 'linear-gradient(90deg, rgb(255, 136, 0)' + x + '%, rgb(24, 29, 39, 0.5)' + x + '%)';
    slider.style.background = color;
})
slider.addEventListener("touchmove", function() {
    var x = slider.value;
    var color = 'linear-gradient(90deg, rgb(255, 136, 0)' + x + '%, rgb(24, 29, 39, 0.5)' + x + '%)';
    slider.style.background = color;
})