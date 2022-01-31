const h1 = document.getElementById("h1")
const h2 = document.getElementById("h2")
const h4 = document.getElementById("h4")
const h8 = document.getElementById("h8")
const h16 = document.getElementById("h16")

const m1 = document.getElementById("m1")
const m2 = document.getElementById("m2")
const m4 = document.getElementById("m4")
const m8 = document.getElementById("m8")
const m16 = document.getElementById("m16")
const m32 = document.getElementById("m32")

const s1 = document.getElementById("s1")
const s2 = document.getElementById("s2")
const s4 = document.getElementById("s4")
const s8 = document.getElementById("s8")
const s16 = document.getElementById("s16")
const s32 = document.getElementById("s32")

const onColor = "#777";
const offColor = "#333"

var time_switch;

function time () {
        now = new Date();
        var strRev = function (str) {
                return str.split("").reverse().join("")
        }
        if (time_switch != now.getSeconds()) {
                hours = strRev((now.getHours()).toString(2))
                minutes = strRev((now.getMinutes()).toString(2))
                seconds = strRev((now.getSeconds()).toString(2))
                h1.style.backgroundColor = hours[0] != "1" ? offColor : onColor;
                h2.style.backgroundColor = hours[1] != "1" ? offColor : onColor;
                h4.style.backgroundColor = hours[2] != "1" ? offColor : onColor;
                h8.style.backgroundColor = hours[3] != "1" ? offColor : onColor;
                h16.style.backgroundColor = hours[4] != "1" ? offColor : onColor;

                m1.style.backgroundColor = minutes[0] != "1" ? offColor : onColor;
                m2.style.backgroundColor = minutes[1] != "1" ? offColor : onColor;
                m4.style.backgroundColor = minutes[2] != "1" ? offColor : onColor;
                m8.style.backgroundColor = minutes[3] != "1" ? offColor : onColor;
                m16.style.backgroundColor = minutes[4] != "1" ? offColor : onColor;
                m32.style.backgroundColor = minutes[5] != "1" ? offColor : onColor;

                s1.style.backgroundColor = seconds[0] != "1" ? offColor : onColor;
                s2.style.backgroundColor = seconds[1] != "1" ? offColor : onColor;
                s4.style.backgroundColor = seconds[2] != "1" ? offColor : onColor;
                s8.style.backgroundColor = seconds[3] != "1" ? offColor : onColor;
                s16.style.backgroundColor = seconds[4] != "1" ? offColor : onColor;
                s32.style.backgroundColor = seconds[5] != "1" ? offColor : onColor;
                console.log("time:", now.getHours() + ":" + now.getMinutes() + ":" + now.getSeconds(),
                    "--> bin:", hours.padStart(6, "0") + ":" + minutes.padStart(6, "0") + ":" + seconds.padStart(6, "0"));
        }
        time_switch = now.getSeconds();
    }

setInterval(time, 1);

//Отображение цифр на часах
function numbers (){
        const nums = document.getElementById("clock");
        const button = document.getElementById("nums")
        console.log(nums.style.color);
        if (nums.style.color == "rgb(204, 204, 204)") {
                nums.style.color = "rgba(0, 0, 0, 0)";
                button.src = "../../static/img/other/nums_on.png";
        } else {
                nums.style.color = "rgb(204, 204, 204)";
                button.src = "../../static/img/other/nums_off.png";
        }
}
