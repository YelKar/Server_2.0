var delay;
function time() {
    var el = document.getElementById("time");
    var now = new Date();
    if (now.getSeconds() != delay) {
        el.innerHTML = now.toLocaleTimeString() + " " + now.toLocaleDateString();
    }
    delay = now.getSeconds();
}

setInterval(time, 1);