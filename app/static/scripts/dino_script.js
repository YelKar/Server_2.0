const dino = document.getElementById("dino")
const cactus = document.getElementById("cactus")
const over = document.getElementById("GameOver")

document.addEventListener("keydown", function (event) {
    console.log(event)
    if (dino.style.animate != "none") {
        switch (event["key"]) {
            case "ArrowUp":
            case " ":
            case "w":
                jump();
                break;
            case "ArrowDown":
                dino.style.backgroundSize = "50px 20px";
                dino.style.height = "20px";
                dino.style.top = "180px";
                setTimeout(function () {
                    dino.style.backgroundSize = "50px 50px";
                    dino.style.height = "50px";
                    dino.style.top = "150px";
                }, 100)
                break;
        }
    } else if (event["key"] == " "){
        location.reload();
    }
});

document.addEventListener("click", function (event) {
    if (dino.style.animate != "none") {
        jump();
    } else {
        location.reload();
    }
})


function jump() {
    if (dino.classList != "jump") {
        dino.classList.add("jump")
    }
    setTimeout(function () {
        dino.classList.remove("jump")
    }, 600)
}

let isAlive = setInterval(function (){
    let dinoTop = parseInt(window.getComputedStyle(dino).getPropertyValue("top"))
    let cactusLeft = parseInt(window.getComputedStyle(cactus).getPropertyValue("left"))

    if (cactusLeft < 25 && cactusLeft > 0 && dinoTop >= 120){
        dino.style.animate = "none";
        cactus.style.display = "none";
        dino.classList.add("die");
        setTimeout(
            function () {
                over.style.visibility = "visible";
            }, 300)
    }
})

console.log(dino);

