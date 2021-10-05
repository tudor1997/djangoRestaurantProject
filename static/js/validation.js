const firstName = document.querySelector(".firstname");
const lastName = document.querySelector(".lastname");
const message = document.querySelector(".message");
const email = document.querySelector(".email");
const form = document.getElementById('form');
const errorElement = document.getElementById('error');

form.addEventListener('submit', (e) => {
    let messages = []
    if(firstName.value == "" || firstName.value == null){
        messages.push("First Name is required");
    }
    if(lastName.value == "" || lastName.value == null){
        messages.push("Last Name is required");
    }
    if(message.value == "" || message.value == null){
        messages.push("A message must be provided.");
    }
    if(email.value == "" || email.value == null){
        messages.push("Email is required");
    }

    if(message.length > 0) {
        e.preventDefault();
        errorElement.innerText = messages.join(', ');
    }

})