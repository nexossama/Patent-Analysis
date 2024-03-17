//Transition -------------------------
const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});


// Captcha ----------------------------

const captchaTextBox = document.querySelector(".captch_box input");
const refreshButton = document.querySelector(".refresh_button");
const captchaInputBox = document.querySelector(".captch_input input");

let captchaText = null;

const generateCaptcha = () => {
  const randomString = Math.random().toString(36).substring(2, 7);
  const randomStringArray = randomString.split("");
  const changeString = randomStringArray.map((char) => (Math.random() > 0.5 ? char.toUpperCase() : char));
  captchaText = changeString.join("     ");
  captchaTextBox.value = captchaText;
};

const refreshBtnClick = () => {
  generateCaptcha();
  captchaInputBox.value = "";
};

function submitCaptcha(){
  captchaText = captchaText
    .split("")
    .filter((char) => char !== " ")
    .join("");
  return captchaInputBox.value === captchaText;
};

refreshButton.addEventListener("click", refreshBtnClick);
generateCaptcha();

// Validation inputs -------------------

const setError = (element, message) => {
  const inputControl = element.parentElement;
  // const errorDisplay = inputControl.querySelector('.error');

  element.value = "";
  element.placeholder = message;
  inputControl.classList.add('error');
  element.classList.add('error2');  // to do??
  inputControl.classList.remove('success');
}

const setSuccess = element => {
  const inputControl = element.parentElement;
  // const errorDisplay = inputControl.querySelector('.error');

  // inputControl.placeholder = '';
  inputControl.classList.add('success');
  inputControl.classList.remove('error');
};

const isValidEmail = email => {
  const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}
// Validation Inscription ------------------------
const sign_up_form = document.getElementsByClassName("sign-up-form")[0];
const username = document.getElementById("username");
const email = document.getElementById("email");
const password1 = document.getElementById("password1");
const password2 = document.getElementById("password2");
const question = document.getElementById("question");
const answer = document.getElementById("answer");
const captcha1 = document.getElementById("captcha1");
const captcha2 = document.getElementById("captcha2");


sign_up_form.addEventListener('submit', e => {
  if (!validateInputsInscription()){
    e.preventDefault();
    // False
  } else {
    // True
  }
});


function validateInputsInscription(){
  var valid = true;

  if(email.value.trim() === '') {
      setError(email, 'Entrer votre email');
      valid = false;
  } else if (!isValidEmail(email.value.trim())) {
      setError(email, 'Entrer un email valide');
      valid = false;
  } else {
      setSuccess(email);
  }

  if(password1.value.trim() === '') {
      setError(password1, 'Entrer un mot de passe');
      valid = false;
  } else if (password1.value.trim().length < 8 ) {
      setError(password1, '8 caractères minimum');
      valid = false;
  } else {
      setSuccess(password1);
  }

  if(password2.value.trim() === '') {
      setError(password2, 'Veuillez confirmer le mot de passe');
      valid = false;
  } else if (password2.value.trim() !== password1.value.trim()) {
      setError(password2, "Les mots de passe ne correspondent pas");
      valid = false;
  } else {
      setSuccess(password2);
  }

  if(captcha2.value === '') {
    setError(captcha2, 'Veillez entrer le code');
    valid = false;
  } else if(submitCaptcha()) {
    setSuccess(captcha2);
  } else {
    setError(captcha2, 'Le code entré est faux');
    valid = false;
  }

  return valid;
};

// Validation Connexion ------------------------
const sign_in_form = document.getElementsByClassName("sign-in-form")[0];
const emailConnexion = document.getElementById("emailConnexion");
const passwordConnexion = document.getElementById("passwordConnexion");

sign_in_form.addEventListener('submit', e => {
  if (!validateInputsConnexion()){
    e.preventDefault();
    // False
  } else {
    // True
  }
});


function validateInputsConnexion(){
  var valid = true;

  if(emailConnexion.value.trim() === '') {
      setError(emailConnexion, 'Entrer votre email');
      valid = false;
  } else if (!isValidEmail(emailConnexion.value.trim())) {
      setError(emailConnexion, 'Entrer un email valide');
      valid = false;
  } else {
      setSuccess(emailConnexion);
  }

  if(passwordConnexion.value.trim() === '') {
      setError(passwordConnexion, 'Entrer un mot de passe');
      valid = false;
  } else if (passwordConnexion.value.trim().length < 8 ) {
      setError(passwordConnexion, '8 caractères minimum');
      valid = false;
  } else {
      setSuccess(passwordConnexion);
  }

  return valid;
};


