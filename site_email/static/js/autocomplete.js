document.getElementById("cliente").addEventListener("keyup", function() {
    var cliente = this.value;
    var sender = document.getElementById("sender").value;
    var edge = document.getElementById("edge").value;
    var vod  = document.getElementById("vod").value;
    document.getElementById("example").innerHTML = "Exemplo de e-mail: <br><br>" +
    "De: " + sender + "<br>" +
    "Para: " + cliente + "<br>" +
    "Olá, tudo bem?<br>"+
    "Somos do suporte técnico da Technobox/CDNTV e percebemos que perdemos a comunicação com o(s) seguinte(s) servidor(es):<br>"+
    "Edge (IP" + edge +")<br>"+
    "VOD (IP" + vod + ")<br>"+
    "Ficamos inteiramente à disposição caso necessitem de algum auxílio técnico. O nosso suporte via WhatsApp/ligação<br>"+
    "funciona de segunda à sábado das 08:30 às 23:00 (horário de Brasília) pelo número (51) 3392-9584. Para suporte fora desses <br>"+
    "horários ou para alguma emergência, estamos disponíveis pelo número de plantão (51) 9 8353-0010, que funciona 24/7 <br>"+
    "Atenciosamente,<br>"
    "Sua assinatura"
    });
    
    document.getElementById("sender").addEventListener("keyup", function() {
    var cliente  = document.getElementById("cliente").value;
    var vod  = document.getElementById("vod").value;
    var edge = document.getElementById("edge").value;
    var sender = this.value;
    document.getElementById("example").innerHTML = "Exemplo de e-mail: <br><br>" +
    "De: " + sender + "<br>" +
    "Para: " + cliente + "<br>" +
    "Olá, tudo bem?<br>"+
    "Somos do suporte técnico da Technobox/CDNTV e percebemos que perdemos a comunicação com o(s) seguinte(s) servidor(es):<br>"+
    "Edge (IP" + edge +")<br>"+
    "VOD (IP" + vod + ")<br>"+
    "Ficamos inteiramente à disposição caso necessitem de algum auxílio técnico. O nosso suporte via WhatsApp/ligação<br>"+
    "funciona de segunda à sábado das 08:30 às 23:00 (horário de Brasília) pelo número (51) 3392-9584. Para suporte fora desses <br>"+
    "horários ou para alguma emergência, estamos disponíveis pelo número de plantão (51) 9 8353-0010, que funciona 24/7 <br>"+
    "Atenciosamente,<br>"
    "Sua assinatura"
    });

    document.getElementById("edge").addEventListener("keyup", function() {
        var cliente = document.getElementById("cliente").value;
        var sender = document.getElementById("sender").value;
        var vod = document.getElementById("vod").value;
        var edge = this.value;
        document.getElementById("example").innerHTML = "Exemplo de e-mail: <br><br>" +
        "De: " + sender + "<br>" +
        "Para: " + cliente + "<br>" +
        "Olá, tudo bem?<br>"+
        "Somos do suporte técnico da Technobox/CDNTV e percebemos que perdemos a comunicação com o(s) seguinte(s) servidor(es):<br>"+
        "Edge (IP" + edge +")<br>"+
        "VOD (IP" + vod + ")<br>"+
        "Ficamos inteiramente à disposição caso necessitem de algum auxílio técnico. O nosso suporte via WhatsApp/ligação<br>"+
        "funciona de segunda à sábado das 08:30 às 23:00 (horário de Brasília) pelo número (51) 3392-9584. Para suporte fora desses <br>"+
        "horários ou para alguma emergência, estamos disponíveis pelo número de plantão (51) 9 8353-0010, que funciona 24/7 <br>"+
        "Atenciosamente,<br>"
        "Sua assinatura"
        });

    document.getElementById("vod").addEventListener("keyup", function() {
        var cliente = document.getElementById("cliente").value;
        var sender = document.getElementById("sender").value;
        var edge = document.getElementById("edge").value;
        var vod = this.value;
        document.getElementById("example").innerHTML = "Exemplo de e-mail: <br><br>" +
    "De: " + sender + "<br>" +
    "Para: " + cliente + "<br>" +
    "Olá, tudo bem?<br>"+
    "Somos do suporte técnico da Technobox/CDNTV e percebemos que perdemos a comunicação com o(s) seguinte(s) servidor(es):<br>"+
    "Edge (IP" + edge +")<br>"+
    "VOD (IP" + vod + ")<br>"+
    "Ficamos inteiramente à disposição caso necessitem de algum auxílio técnico. O nosso suporte via WhatsApp/ligação<br>"+
    "funciona de segunda à sábado das 08:30 às 23:00 (horário de Brasília) pelo número (51) 3392-9584. Para suporte fora desses <br>"+
    "horários ou para alguma emergência, estamos disponíveis pelo número de plantão (51) 9 8353-0010, que funciona 24/7 <br>"+
    "Atenciosamente,<br>"
    "Sua assinatura"
        });
    
    // Exibe o exemplo de e-mail assim que a página é carregada
    document.getElementById("cliente").dispatchEvent(new Event("keyup"));
    document.getElementById("sender").dispatchEvent(new Event("keyup"));
    document.getElementById("edge").dispatchEvent(new Event("keyup"));
    document.getElementById("vod").dispatchEvent(new Event("keyup"));