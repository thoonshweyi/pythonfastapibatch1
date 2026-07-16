// UI

console.log("hello");
var ws = new WebSocket("ws://localhost:8000/ws");

const sendbtn = document.getElementById('send-btn');
const userinput = document.getElementById('userinput');
const displaybox = document.getElementById('displaybox');

var ws = new WebSocket("ws://localhost:8000/ws");

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
     // console.log(event.data);
     let message = event.data;
     if(message){
          let messagediv = document.createElement('div');
          messagediv.className = "p-3 ms-3 chat-message ai-response";
          messagediv.textContent = message;
          displaybox.appendChild(messagediv);

          document.getElementById('loading-spinner').style.display = "none";
     }

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

          document.getElementById('loading-spinner').style.display = "block";
     }
});
