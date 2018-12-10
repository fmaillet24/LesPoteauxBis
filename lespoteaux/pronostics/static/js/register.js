var elementConfirm = document.getElementById('confirm-password');
elementConfirm.addEventListener('input', function(e){
  e.preventDefault();
  var get_password = document.getElementById('password');
  var password = get_password.value;
  var confirm = elementConfirm.value;

  if (password === confirm){
    createValidation();
  }else{
    createCross();
  }
})

function createValidation(){
  var confirmInput = document.getElementById('confirm-password');
  var createCheck = document.createElement('i');
  createCheck.setAttribute('class', 'fas fa-check');
  confirmInput.appendChild(createCheck);
}

function createCross(){
  var confirmInput = document.getElementById('confirm-password');
  var createCross = document.createElement('i');
  createCross.setAttribute('class', 'fas fa-times-circle');
  confirmInput.appendChild(createCross);
}

function cleanElement(){
  var confirmInput = document.getElementById('confirm-password');
  if (confirmInput){

  }
}
