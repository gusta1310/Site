document.addEventListener("DOMContentLoaded", function() {
    const elemento = document.getElementById("maquina-escrever");
    const textoOriginal = "Por que Empreender Desde Cedo?";
    const cor = '<span style="color: blue;">Empreender</span>';
    const partes = textoOriginal.split("Empreender");
    const textoFinal = partes[0] + cor + partes[1];
    let i = 0;
    elemento.innerHTML = "";

    function escrever() {
        if (i <= partes[0].length) {
            elemento.innerHTML = partes[0].substring(0, i);
        } else if (i <= partes[0].length + "Empreender".length) {
            elemento.innerHTML = partes[0] + '<span style="color: blue;">' + "Empreender".substring(0, i - partes[0].length) + '</span>';
        } else {
            elemento.innerHTML = partes[0] + '<span style="color: blue;">Empreender</span>' + partes[1].substring(0, i - partes[0].length - "Empreender".length);
        }
        i++;
        if (i <= textoOriginal.length) {
            setTimeout(escrever, 80);
        }
    }
    escrever();
});