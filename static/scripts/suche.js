document.getElementById("query_btn").addEventListener("click", function() {
    let first_name = document.querySelector("#validationServer01").value;
    let last_name = document.querySelector("#validationServer02").value;
    let company = document.querySelector("#validationServer03").value;
    let mail = document.querySelector("#validationServer04").value;
    let tel = document.querySelector("#validationServer05").value;

    var query_url = "http://127.0.0.1:5000/query?";
    if(first_name.localeCompare("") != 0){
        query_url = query_url.concat("first=".concat(first_name))
    }
    if(last_name.localeCompare("") != 0){
        if(query_url.charAt(query_url.length-1) == '?'){
            query_url = query_url.concat("last=".concat(last_name))
        }
        else{
            query_url = query_url.concat("&last=".concat(last_name))
        }
    }
    if(company.localeCompare("") != 0){
        if(query_url.charAt(query_url.length-1) == '?'){
            query_url = query_url.concat("company=".concat(company))
        }
        else{
            query_url = query_url.concat("&company=".concat(company))
        }
    }
    if(mail.localeCompare("") != 0){
        if(query_url.charAt(query_url.length-1) == '?'){
            query_url = query_url.concat("mail=".concat(mail))
        }
        else{
            query_url = query_url.concat("&mail=".concat(mail))
        }
    }
    if(tel.localeCompare("") != 0){
        if(query_url.charAt(query_url.length-1) == '?'){
            query_url = query_url.concat("tel=".concat(tel))
        }
        else{
            query_url = query_url.concat("&tel=".concat(tel))
        }
    }
    //get Request with query_url
    var Httpreq = new XMLHttpRequest(); // a new request
    Httpreq.open("GET",query_url,false);
    Httpreq.send(null);
    var json_answer = Httpreq.response;
    console.log(json_answer)

    var col = [];
    for (var i = 0; i < json_answer.length; i++) {
        for (var key in json_answer[i]) {
            if (col.indexOf(key) === -1) {
                col.push(key);
            }
        }
    }
    console.log(col)
});