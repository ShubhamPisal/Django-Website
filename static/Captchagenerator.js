function createCaptcha() {
    // clear the contents of captcha div first 
    var canvas = document.getElementById("captcha");
    var ctx = canvas.getContext("2d");
    ctx.fillstyle = "red";
    ctx.textAlign ="center";
    ctx.font = "25px Georgia";
    ctx.strokeText("{{cap}}", canvas.width/2, canvas.height/2);
//    document.getElementById('captcha').innerHTML = "";
//    var captcha = {{random_string}};
//    var canv = document.createElement("canvas");
//    canv.id = "captcha";
//    canv.width = 100;
//    canv.height = 38;
//    var ctx = canv.getContext("2d");
//    ctx.font = "25px Georgia";
//    ctx.strokeText(captcha.join(""), 0, 30);
//    //storing captcha so that can validate you can save it somewhere else according to your specific requirements
//    code = captcha.join("");
//    document.getElementById("captcha").appendChild(canv); // adds the canvas to the body element 
}

function EnableDisable(cpatchaTextBox) {
//Reference the Button.
    var btnSubmit = document.getElementById("login");
    
//Verify the TextBox value.
    if (cpatchaTextBox.value.trim() == "{{cap}}") {
    
//Enable the Login when cpatchaTextBox has value.
    btnSubmit.disabled = false;
    } else {
    
//Disable the Login when cpatchaTextBox is empty.
    btnSubmit.disabled = true;
    }
    }