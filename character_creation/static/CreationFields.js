let inputFields = document.getElementsByClassName("num_checker");
let value = document.getElementById("points");

mainfunc = () => {
    for (let i=0; i < inputFields.length; i++) {
        inputFields[i].onchange = checkField(inputFields[i]);
        console.log(inputFields[i]);
    }
};


checkField = inputField => {
    if (inputField.value < 0 || (value - inputField.value) < 0) {
        inputField.value = 0;
    }
    else if (inputField.value > 0 && (value - inputField.value) > 0) {
        value.innerHTML = (value - inputField.value);
    }
};

mainfunc();
