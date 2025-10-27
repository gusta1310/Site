document.addEventListener("DOMContentLoaded", function() {
    const elemento = document.getElementById("maquina-escrever");
    const textoOriginal = "Por que Empreender desde cedo?";
    const partes = textoOriginal.split("Empreender");
    let i = 0;
    elemento.innerHTML = "";

    function escrever() {
        if (i <= partes[0].length) {
            elemento.innerHTML = partes[0].substring(0, i);
        } else if (i <= partes[0].length + "Empreender".length) {
            elemento.innerHTML = partes[0] + '<span style="color: #e1b239;">' + "Empreender".substring(0, i - partes[0].length) + '</span>';
        } else {
            elemento.innerHTML = partes[0] + '<span style="color: #e1b239;">Empreender</span>' + partes[1].substring(0, i - partes[0].length - "Empreender".length);
        }
        i++;
        if (i <= textoOriginal.length) {
            setTimeout(escrever, 80);
        }
    }
    escrever();
});