var host = "http://192.168.1.3:2222"
var get = "/messenger/get_messages"
var send = "/messenger/send_messages"
after = 0

var messenger = document.getElementById("messenger")


function httpGet(url) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url, false ); // false for synchronous request
    xmlHttp.send( null );
    return JSON.parse(xmlHttp.responseText);
}

var json = httpGet(get)["messages"];



function to_document() {
    var p = document.getElementById("mess")
    var json = httpGet(get)["messages"]
    ans = ""
    for (var message in json) {
        message = json[message]
        var timestamp = new Date(message["timestamp"]);
        ans += `
<fieldset>
    <legend>${message["username"]}</legend>\n
    <p class="message">${message["text"]}</p>\n
    <p class"timestamp">${timestamp.toLocaleTimeString()} ${timestamp.toLocaleDateString()}</p>
</fieldset>
            
        `
    }
    p.innerHTML = ans;
}

function listen(){
    var messenger = document.getElementById("messenger")
    var scroll = messenger.scrollTop + messenger.offsetHeight;
    var height = messenger.offsetHeight;
    var new_json = httpGet(get)["messages"];
    console.log(json == new_json, json, new_json)
    if (json.length != new_json.length) {
        json = new_json
        if (scroll >= height - 10) {
            messenger.scrollTo(0, 9999999)
        }
    }

}

function send_message(username="Anonymous", text="Text"){
    if (!username) {
        username = "Anonymous";
    }
    var time = new Date();
    var message = {
        "username": username,
        "text": text,
        "timestamp": time.getTime()
    }
    fetch(
        send, {
            method: "POST",
            body: JSON.stringify(message),
            headers: {
              'Content-Type': 'application/json'
            }
        }
    )
}

function enterMessage() {
    var textarea = document.getElementById("text_in")
    var username = document.getElementById("username")
    send_message(username.value, textarea.value)
    console.log(username.value)
    textarea.value = "";
}

listen()
to_document()
setTimeout(function () {messenger.scrollTo(0, 999999)}, 10)
setInterval(listen, 1000)
