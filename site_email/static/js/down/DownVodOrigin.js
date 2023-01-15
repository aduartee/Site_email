document.getElementById("cliente").addEventListener("keyup", function() {
    var cliente = this.value;
    var vod = document.getElementById("vod").value;
    var origin = document.getElementById("origin").value;
    var demanda = document.getElementById("demanda").value;
    var provedor = document.getElementById("provedor").value;
    document.getElementById("example").innerHTML = "Exemplo de e-mail: <br><br>" + "Assunto: [CDNTV Suporte #" + demanda + "] - " + provedor + " - Origin e Vod Down <br><br>" + 
    "De: seuemail@email.com <br>" + "Para: " + cliente + "<br><br>" + 
    "Olá, tudo bem?<br><br>" + 
    "Somos do suporte técnico da Technobox/CDNTV e percebemos que perdemos a comunicação com o(s) seguinte(s) servidor(es):<br><br>" + 
    "Origin(IP: " + origin + ")<br>"+ 
    "Vod(IP: " + vod + ")<br>"+ 
    "Ficamos inteiramente à disposição caso necessitem de algum auxílio técnico. O nosso suporte via WhatsApp/ligação<br><br>" + 
    "funciona de segunda à sábado das 08:30 às 23:00 (horário de Brasília) pelo número (51) 3392-9584. Para suporte fora desses <br>" + 
    "horários ou para alguma emergência, estamos disponíveis pelo número de plantão (51) 9 8353-0010, que funciona 24/7 <br><br><br>" + 
    "Atenciosamente,<br>" + 
    "Sua assinatura"
});

document.getElementById("origin").addEventListener("keyup", function() {
    var cliente = document.getElementById("cliente").value;
    var demanda = document.getElementById("demanda").value;
    var provedor = document.getElementById("provedor").value;
    var vod = document.getElementById("vod").value;
    var origin = this.value;
    document.getElementById("example").innerHTML = "Exemplo de e-mail: <br><br>" + "Assunto: [CDNTV Suporte #" + demanda + "] - " + provedor + " - Origin e Vod Down <br><br>" + 
    "De: seuemail@email.com <br>" + "Para: " + cliente + "<br><br>" + 
    "Olá, tudo bem?<br><br>" + 
    "Somos do suporte técnico da Technobox/CDNTV e percebemos que perdemos a comunicação com o(s) seguinte(s) servidor(es):<br><br>" + 
    "Origin(IP: " + origin + ")<br>"+ 
    "Vod(IP: " + vod + ")<br>"+
    "Ficamos inteiramente à disposição caso necessitem de algum auxílio técnico. O nosso suporte via WhatsApp/ligação<br><br>" + 
    "funciona de segunda à sábado das 08:30 às 23:00 (horário de Brasília) pelo número (51) 3392-9584. Para suporte fora desses <br>" + 
    "horários ou para alguma emergência, estamos disponíveis pelo número de plantão (51) 9 8353-0010, que funciona 24/7 <br><br><br>" + 
    "Atenciosamente,<br>" + 
    "Sua assinatura"
});

document.getElementById("vod").addEventListener("keyup", function() {
    var cliente = document.getElementById("cliente").value;
    var demanda = document.getElementById("demanda").value;
    var provedor = document.getElementById("provedor").value;
    var origin = document.getElementById("origin").value;
    var vod = this.value;
    document.getElementById("example").innerHTML = "Exemplo de e-mail: <br><br>" + "Assunto: [CDNTV Suporte #" + demanda + "] - " + provedor + " - Origin e Vod Down <br><br>" + 
    "De: seuemail@email.com <br>" + "Para: " + cliente + "<br><br>" + 
    "Olá, tudo bem?<br><br>" + 
    "Somos do suporte técnico da Technobox/CDNTV e percebemos que perdemos a comunicação com o(s) seguinte(s) servidor(es):<br><br>" + 
    "Origin(IP: " + origin + ")<br>"+ 
    "Vod(IP: " + vod + ")<br>"+
    "Ficamos inteiramente à disposição caso necessitem de algum auxílio técnico. O nosso suporte via WhatsApp/ligação<br><br>" + 
    "funciona de segunda à sábado das 08:30 às 23:00 (horário de Brasília) pelo número (51) 3392-9584. Para suporte fora desses <br>" + 
    "horários ou para alguma emergência, estamos disponíveis pelo número de plantão (51) 9 8353-0010, que funciona 24/7 <br><br><br>" + 
    "Atenciosamente,<br>" + 
    "Sua assinatura"
});

document.getElementById("demanda").addEventListener("keyup", function() {
    var cliente = document.getElementById("cliente").value;
    var vod = document.getElementById("vod").value;
    var origin = document.getElementById("origin").value;
    var demanda = this.value;
    var provedor = document.getElementById("provedor").value;
    document.getElementById("example").innerHTML = "Exemplo de e-mail: <br><br>" + "Assunto: [CDNTV Suporte #" + demanda + "] - " + provedor + " - Origin e Vod Down <br><br>" + 
    "De: seuemail@email.com <br>" + "Para: " + cliente + "<br><br>" + 
    "Olá, tudo bem?<br><br>" + 
    "Somos do suporte técnico da Technobox/CDNTV e percebemos que perdemos a comunicação com o(s) seguinte(s) servidor(es):<br><br>" + 
    "Origin(IP: " + origin + ")<br>"+ 
    "Vod(IP: " + vod + ")<br>"+
    "Ficamos inteiramente à disposição caso necessitem de algum auxílio técnico. O nosso suporte via WhatsApp/ligação<br><br>" + 
    "funciona de segunda à sábado das 08:30 às 23:00 (horário de Brasília) pelo número (51) 3392-9584. Para suporte fora desses <br>" + 
    "horários ou para alguma emergência, estamos disponíveis pelo número de plantão (51) 9 8353-0010, que funciona 24/7 <br><br><br>" + 
    "Atenciosamente,<br>" + 
    "Sua assinatura"
});

document.getElementById("provedor").addEventListener("keyup", function() {
    var cliente = document.getElementById("cliente").value;
    var vod = document.getElementById("vod").value;
    var origin = document.getElementById("origin").value;
    var demanda = document.getElementById("demanda").value;
    var provedor = this.value;
    document.getElementById("example").innerHTML = "Exemplo de e-mail: <br><br>" + "Assunto: [CDNTV Suporte #" + demanda + "] - " + provedor + " - Origin e Vod Down <br><br>" + 
    "De: seuemail@email.com <br>" + "Para: " + cliente + "<br><br>" + 
    "Olá, tudo bem?<br><br>" + 
    "Somos do suporte técnico da Technobox/CDNTV e percebemos que perdemos a comunicação com o(s) seguinte(s) servidor(es):<br><br>" + 
    "Origin(IP: " + origin + ")<br>"+ 
    "Vod(IP: " + vod + ")<br>"+
    "Ficamos inteiramente à disposição caso necessitem de algum auxílio técnico. O nosso suporte via WhatsApp/ligação<br><br>" + 
    "funciona de segunda à sábado das 08:30 às 23:00 (horário de Brasília) pelo número (51) 3392-9584. Para suporte fora desses <br>" + 
    "horários ou para alguma emergência, estamos disponíveis pelo número de plantão (51) 9 8353-0010, que funciona 24/7 <br><br><br>" + 
    "Atenciosamente,<br>" + 
    "Sua assinatura"
}); 

// Exibe o exemplo de e-mail assim que a página é carregada     
    document.getElementById("cliente").dispatchEvent(new Event("keyup"));     
    document.getElementById("vod").dispatchEvent(new Event("keyup"));     
    document.getElementById("origin").dispatchEvent(new Event("keyup"));  
    document.getElementById("demanda").dispatchEvent(new Event("keyup"));     
    document.getElementById("provedor").dispatchEvent(new Event("keyup"));