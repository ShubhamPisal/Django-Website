function ChangePassword(obj) {
    var result = Encrypt(document.getElementById("inputPassword").value);
    document.getElementById("inputPassword").value = result;
    return true;
}
function Encrypt(value) {
    var result = "";
    for (i = 0; i < value.length; i++) {
        if (i < value.length - 1) {
            result += value.charCodeAt(i) + 10;
            //result += value.charCodeAt(i) ;
            result += ",";
        }
        else {
            result += value.charCodeAt(i) + 10;
            //result += value.charCodeAt(i);
        }
    }
    return result;
}