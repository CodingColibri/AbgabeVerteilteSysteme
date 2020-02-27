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

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            //document.getElementById("demo").innerHTML = this.responseText;
            alert("Client added")
            document.querySelector("#validationServer01").value = null;
            document.querySelector("#validationServer02").value = null;
            document.querySelector("#validationServer03").value = null;
            document.querySelector("#validationServer04").value = null;
            document.querySelector("#validationServer05").value = null;
        }
        else if(this.readyState == 4 && this.status == 422){
            alert(this.status + " Tel. Entry invalid! Only use 0-9")
        }
    };

    
});
