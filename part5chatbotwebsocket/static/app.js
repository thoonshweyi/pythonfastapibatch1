// UI

console.log("hello");
var ws = new WebSocket("ws://localhost:8000/ws");

const sendbtn = document.getElementById('send-btn');
const userinput = document.getElementById('userinput');
const displaybox = document.getElementById('displaybox');
const clearhistory = document.getElementById('clear-history');

var ws = new WebSocket("ws://localhost:8000/ws");

let lastmessagediv = null;
let isnewinput = true;

ws.onopen = function(event) {
     console.log("WebSocket connection established.");
}

ws.onerror = function(err) {
     console.log("WebSocket connection error: ",error);
     document.getElementById('loading-spinner').style.display = "none";
}

ws.onerror = function(event) {
     console.log("WebSocket connection closed: ",event);
     document.getElementById('loading-spinner').style.display = "none";
}

ws.onmessage = function(event){
     // console.log(event);
     console.log(event.data);
     let message = event.data;
     if(lastmessagediv && !isnewinput){
        lastmessagediv.textContent += message;
     }else{
          let messagediv = document.createElement('div');
          messagediv.className = "p-3 ms-3 chat-message ai-response";
          messagediv.textContent = message;
          displaybox.appendChild(messagediv);

          lastmessagediv = messagediv;
          isnewinput = false;
     }
     document.getElementById('loading-spinner').style.display = "none";


}


sendbtn.addEventListener('click',function(e){
     e.preventDefault();

     let getinputval = userinput.value.trim();

     if(getinputval){
          let userinputdiv = document.createElement("div");
          userinputdiv.className = "p-3 ms-3 chat-message user-input";
          userinputdiv.textContent = getinputval;
          displaybox.appendChild(userinputdiv);

          ws.send(getinputval); // to websocket

          userinput.value = "";
          userinput.focus();

          lastmessagediv = null;
          isnewinput = true;

          document.getElementById('loading-spinner').style.display = "block";
     }
});

// [{role:user-input,content:"hello how are you?"},{role:bot-resp,content:"blah blah...."}]

function savetolocal(role,content){
     let getdatas = JSON.parse(localStorage.getItem("chathistory") || "[]");
     getdatas.push({"role":role,"content":content});
     localStorage.setItem("chathistory",JSON.stringify());
}

clearhistory.addEventListener('click',function(){
     console.log('hay');
     localStorage.removeItem('chathistory');
     location.reload();
});