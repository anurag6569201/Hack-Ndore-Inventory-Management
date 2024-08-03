let signin=document.getElementById("welcome_signin");
let signup=document.getElementById("welcome_signup");

function signup_visible(){
    signin.style.display="none";
    signup.style.display="block";
}

function signin_visible(){
    signin.style.display="block";
    signup.style.display="none";
}