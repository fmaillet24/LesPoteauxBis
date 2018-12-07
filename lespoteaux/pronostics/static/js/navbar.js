var burger = document.getElementById('burger')
burger.addEventListener('click', function(e){
  e.preventDefault();
  openNav();
})

var cross = document.getElementById('cross')
cross.addEventListener('click', function(e){
  e.preventDefault();
  closeNav();
})

function openNav(){
  document.getElementById("block-mobile").style.width = "100%";
}

function closeNav(){
  document.getElementById("block-mobile").style.width = "0";
}
