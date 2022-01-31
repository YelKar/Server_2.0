// Прокрутка меню
function scroll_menu() {
    if (window.innerWidth < 991) return
    const main = document.querySelector("main")
    const menu = document.getElementById("menu")
    const menu2 = document.getElementsByClassName("menu_open")
    const header_height = 100
    const clientHeight = document.documentElement.clientHeight - header_height * (window.scrollY <= header_height) + window.scrollY * (window.scrollY <= header_height) + "px"

    menu2[0].style.height = menu2[1].style.height = clientHeight

    if (window.scrollY >= header_height && main.offsetHeight > window.innerHeight) {
        menu.style.position = "fixed";
        menu.style.marginTop = "0";
        menu2[0].style.marginTop = "0";
        menu2[1].style.marginTop = "0";

    // } else if (window.scrollY == "0") {
    //     menu.style.position = "fixed";
    //     menu.style.marginTop = header_height + "px";
    }
    else {
        menu.style.position = "absolute";
        menu.style.marginTop = header_height + "px";
    }
    // console.log(`window.scrollY: ${window.scrollY}\n`, `window.scrollY == "0": ${window.scrollY == "0"}\n`, `window.scrollY > 0: ${window.scrollY > 0}\n`, document.documentElement.clientHeight)
}


// Определение операционной системы
function detectOs() {
    var info = navigator.appVersion.toLowerCase();
    if (/android/.test(info)) return "Android";
    if (/linux/.test(info)) return "Linux";
    if (/windows/.test(info)) return "Windows";
    if (/mac/.test(info)) return "MacOS";
    if (/iphone|ipad|ipod|ipod touch/) return "iOS";
    return "unknown";
}
function detectClient() {
    var info = navigator.userAgent.toLowerCase();
    if (/edg/.test(info)) return "Microsoft Edge"
    if (/opr/.test(info)) return "Opera"
    if (/firefox/.test(info)) return "Mozilla Firefox"
    return "Google Chrome"
}


setInterval(scroll_menu, 1)