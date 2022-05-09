var cvs = document.getElementById("canvas")
var ctx = cvs.getContext("2d")

var bird = new Image()
bird.fall = new Image()
bird.up = new Image()
bird.down = new Image()
var bg = new Image()
var fg = new Image()
var pipeUp = new Image()
var pipeBottom = new Image()

var img_route = "../../static/img/other/flappyBird/"

bird.src = img_route + "big_bird.png"
bird.fall.src = img_route + "bird_fall.png"
bird.up.src = img_route + "bird_up.png"
bird.down.src = img_route + "bird_down.png"
bg.src = img_route + "bg.png"
fg.src = img_route + "fg.png"
pipeUp.src = img_route + "pipeUp.png"
pipeBottom.src = img_route + "pipeBottom.png"

var start = true;

// При нажатии на кнопку
document.addEventListener("keydown", moveUp)
document.addEventListener("click", moveUp)


function moveUp() {
    if (start) {
        start = false;
        create()
        draw()
    }
    grav = -6;
}

// Создание блоков
var pipe = [];


var score = 0;
var pipes_pos = -50;
var gap = 190;

// П// Позиция птички
var xPos = 10;
var yPos = 150;
var grav = 0;

var run = true;
var render_bird = bird;
var boost = false
var hit = true;

function create() {
    pipe = [];

    pipe[0] = {
        x: cvs.width,
        y: -100,
        gap: gap
    }

    score = 0;
    pipes_pos = -50;
    gap = 190;

    // Позиция птички
    xPos = 10;
    yPos = 150;
    grav = 0;

    run = true;
}
create()
function wait() {
    ctx.drawImage(bg, 0, 0)
    ctx.drawImage(fg, 0, cvs.height - fg.height)
    ctx.drawImage(bird, xPos, yPos)
}

function draw() {
    ctx.drawImage(bg, 0, 0)
    for (var i in pipe){
        ctx.drawImage(pipeUp, pipe[i].x, pipe[i].y)
        ctx.drawImage(pipeBottom, pipe[i].x, pipe[i].y + pipeUp.height + pipe[i].gap)

        pipe[i].x -= (1 + boost);

        if (pipe[i].x == 125 || (pipe[i].x == 126 && boost)) {
            pipe.push({
                x: cvs.width,
                y: pipes_pos - gap / 2 + (Math.random() - 0.5) * ((cvs.height - gap) / 2),
                gap: gap
            });
        }

        if ((
            xPos + bird.width - 5 >= pipe[i].x
            && xPos <= pipe[i].x + pipeUp.width
            && (yPos + 8 <= pipe[i].y + pipeUp.height
                || yPos + bird.height - 8 >= pipe[i].y + pipeUp.height + gap)
            || yPos + bird.height - 8 >= cvs.height - fg.height)
            && hit
        ){
            run = false
        }

        if (pipe[i].x == 5) {
            score++;
        }
        if (score == 10) {
            gap = 160;
        } if (score == 20) {
            gap == 130;
        } if (score == 30) {
            gap == 100;
        } if (score == 60) {
            gap = 90;
        }

    }
    render_bird = function () {
        if (grav >= -1 && grav <= 4) return bird;
        if (grav < -1) return bird.up;
        if (grav == 10) return bird.fall;
        return bird.down;
    }()
    ctx.drawImage(fg, 0, cvs.height - fg.height)
    ctx.drawImage(render_bird, xPos, yPos)
    yPos += grav;
    grav += 0.5;

    ctx.fillStyle = "#000"
    ctx.font = "20px Calibri"
    ctx.fillText("Счет: " + score, 10, cvs.height - 20)

    if (grav >= 10) {
        grav = 10;
    }
    if (run) {
        requestAnimationFrame(draw)
    } else {
        setTimeout(function () {
            start = true;
        }, 1000)
    }
}

document.addEventListener('keydown', function(event) {
    boost = /Shift/.test(event.code) && run;
});

pipeBottom.onload = wait;
