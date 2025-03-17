// UI
const sendbtn = document.getElementById('send-btn');
const userinput = document.getElementById('userinput');
const displaybox = document.getElementById('displaybox');

sendbtn.addEventListener('click',function(e){
     e.preventDefault();

     console.log('sendbtn clicked');
});