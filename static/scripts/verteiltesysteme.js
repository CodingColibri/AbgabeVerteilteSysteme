document.getElementById("bs").addEventListener("click", function() {
    let first_name = document.querySelector("#validationServer01").value;
    let last_name = document.querySelector("#validationServer02").value;
    let company = document.querySelector("#validationServer03").value;
    let mail = document.querySelector("#validationServer04").value;
    let tel = document.querySelector("#validationServer05").value;
    var client = {
        "first_name": first_name,
        "last_name": last_name,
        "company": company,
        "mail": mail,
        "tel": tel
    };
    var xhr = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    var data = JSON.stringify(client);
    xhr.send(data);

    alert("Client wurde registriert. Whup Whup. ");
    document.querySelector("#validationServer01").value = null;
    document.querySelector("#validationServer01").value;
    document.querySelector("#validationServer01").value;
    document.querySelector("#validationServer01").value;
    document.querySelector("#validationServer01").value;
});