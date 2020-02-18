var eingabe = document.querySelector('#eingabe');

document.getElementById("bestaetigen").addEventListener("click", wertauslesen);

function wertauslesen() {
    var wert = eingabe.value;
    alert(wert);
    eingabe.value = null;
};