document.getElementById("origin").addEventListener("keyup", function() {
    var origin = this.value;
    var senha = document.getElementById("senha").value;
    var edge = document.getElementById("edge").value;
    var email = document.getElementById("email").value;
    var demanda = document.getElementById("demanda").value;
    var provedor = document.getElementById("provedor").value;

    document.getElementById("example").innerHTML = "Exemplo de e-mail: <br><br>" + 
    "Assunto: [CDNTV #" + demanda + "] - " + provedor + " - Instalação <br><br>" +
    "De: seuemail@email.com <br>" + "Para: " + email + "<br><br>" +
    "Olá, tudo bem? <br><br>" +
    "Informamos que a CDNTV (Origin/Edge) foi instalada com sucesso na sua estrutura. Já é possível acessar o centro de gerenciamento" +
    "da CDNTV (CDNTV Manager) através dos acessos abaixo mencionados. Através desta central é possível: gerenciar canais, usuários e firewall," +
    "além de visualizar as estatísticas de acesso. <br><br>" +
    "Foram configurados dois servidores para sua CDNTV: <br><br>" +
    "Origin - Responsável pela gerência da CDNTV e pela recepção dos fluxos. <br>" +
    "Edge - Responsável pelo player web e pela distribuição dos fluxos. <br><br>" +
    "-- <br><br>" +
    "Origin: " + origin + "<br><br>" +
    "Usuário: admin <br>" +
    "Senha: "+ senha +" <br><br>" +
    "-- <br><br>" +
    "Edge : " + edge +" <br><br>" +
    "Usuário: cliente <br>" +
    "Senha: cliente <br><br>" +
    "-- <br><br>" +
    "Terminada a instalação dos servidores, já enviamos as imagens para a geração das aplicações. <br><br>" +
    "Em adição, você pode conferir nossa documentação completa para o uso da plataforma clicando aqui. <br><br>" +
    "No menu “Guias e Processos” encontram-se os tutoriais do passo-a-passo inicial (Começando) e da administração" +
    "da interface web (Painel de Administração), contendo vídeos explicativos para o uso de todas as funções disponíveis" +
    "na plataforma. <br><br> -- <br><br>" +
    "O nosso suporte via Skype funciona de segunda à sexta, das 08:30 às 23:00, e aos sábados, das 09:00 às 17:30 (horário de Brasília)." + 
    "Para suporte relacionado a problemas ou alguma emergência, possuímos o número plantão - (51) 98353 0000, que funciona 24 horas, todos os dias. <br><br>" +
    "Atenciosamente,"
});

document.getElementById("senha").addEventListener("keyup", function() {
    var origin = document.getElementById("origin").value;
    var senha = this.value;
    var edge = document.getElementById("edge").value;
    var email = document.getElementById("email").value;
    var demanda = document.getElementById("demanda").value;
    var provedor = document.getElementById("provedor").value;

    document.getElementById("example").innerHTML = "Exemplo de e-mail: <br><br>" + 
    "Assunto: [CDNTV #" + demanda + "] - " + provedor + " - Instalação <br><br>" +
    "De: seuemail@email.com <br>" + "Para: " + email + "<br><br>" +
    "Olá, tudo bem? <br><br>" +
    "Informamos que a CDNTV (Origin/Edge) foi instalada com sucesso na sua estrutura. Já é possível acessar o centro de gerenciamento" +
    "da CDNTV (CDNTV Manager) através dos acessos abaixo mencionados. Através desta central é possível: gerenciar canais, usuários e firewall," +
    "além de visualizar as estatísticas de acesso. <br><br>" +
    "Foram configurados dois servidores para sua CDNTV: <br><br>" +
    "Origin - Responsável pela gerência da CDNTV e pela recepção dos fluxos. <br>" +
    "Edge - Responsável pelo player web e pela distribuição dos fluxos. <br><br>" +
    "-- <br><br>" +
    "Origin: " + origin + "<br><br>" +
    "Usuário: admin <br>" +
    "Senha: "+ senha +" <br><br>" +
    "-- <br><br>" +
    "Edge : " + edge +" <br><br>" +
    "Usuário: cliente <br>" +
    "Senha: cliente <br><br>" +
    "-- <br><br>" +
    "Terminada a instalação dos servidores, já enviamos as imagens para a geração das aplicações. <br><br>" +
    "Em adição, você pode conferir nossa documentação completa para o uso da plataforma clicando aqui. <br><br>" +
    "No menu “Guias e Processos” encontram-se os tutoriais do passo-a-passo inicial (Começando) e da administração" +
    "da interface web (Painel de Administração), contendo vídeos explicativos para o uso de todas as funções disponíveis" +
    "na plataforma. <br><br> -- <br><br>" +
    "O nosso suporte via Skype funciona de segunda à sexta, das 08:30 às 23:00, e aos sábados, das 09:00 às 17:30 (horário de Brasília)." + 
    "Para suporte relacionado a problemas ou alguma emergência, possuímos o número plantão - (51) 98353 0000, que funciona 24 horas, todos os dias. <br><br>" +
    "Atenciosamente,"
});

document.getElementById("edge").addEventListener("keyup", function() {
    var origin = document.getElementById("origin").value;
    var senha = document.getElementById("senha").value;
    var edge = this.value;
    var email = document.getElementById("email").value;
    var demanda = document.getElementById("demanda").value;
    var provedor = document.getElementById("provedor").value;

    document.getElementById("example").innerHTML = "Exemplo de e-mail: <br><br>" + 
    "Assunto: [CDNTV #" + demanda + "] - " + provedor + " - Instalação <br><br>" +
    "De: seuemail@email.com <br>" + "Para: " + email + "<br><br>" +
    "Olá, tudo bem? <br><br>" +
    "Informamos que a CDNTV (Origin/Edge) foi instalada com sucesso na sua estrutura. Já é possível acessar o centro de gerenciamento" +
    "da CDNTV (CDNTV Manager) através dos acessos abaixo mencionados. Através desta central é possível: gerenciar canais, usuários e firewall," +
    "além de visualizar as estatísticas de acesso. <br><br>" +
    "Foram configurados dois servidores para sua CDNTV: <br><br>" +
    "Origin - Responsável pela gerência da CDNTV e pela recepção dos fluxos. <br>" +
    "Edge - Responsável pelo player web e pela distribuição dos fluxos. <br><br>" +
    "-- <br><br>" +
    "Origin: " + origin + "<br><br>" +
    "Usuário: admin <br>" +
    "Senha: "+ senha +" <br><br>" +
    "-- <br><br>" +
    "Edge : " + edge +" <br><br>" +
    "Usuário: cliente <br>" +
    "Senha: cliente <br><br>" +
    "-- <br><br>" +
    "Terminada a instalação dos servidores, já enviamos as imagens para a geração das aplicações. <br><br>" +
    "Em adição, você pode conferir nossa documentação completa para o uso da plataforma clicando aqui. <br><br>" +
    "No menu “Guias e Processos” encontram-se os tutoriais do passo-a-passo inicial (Começando) e da administração" +
    "da interface web (Painel de Administração), contendo vídeos explicativos para o uso de todas as funções disponíveis" +
    "na plataforma. <br><br> -- <br><br>" +
    "O nosso suporte via Skype funciona de segunda à sexta, das 08:30 às 23:00, e aos sábados, das 09:00 às 17:30 (horário de Brasília)." + 
    "Para suporte relacionado a problemas ou alguma emergência, possuímos o número plantão - (51) 98353 0000, que funciona 24 horas, todos os dias. <br><br>" +
    "Atenciosamente,"
});

document.getElementById("email").addEventListener("keyup", function() {
    var origin = document.getElementById("origin").value;
    var senha = document.getElementById("senha").value;
    var edge = document.getElementById("edge").value;
    var email = this.value;
    var demanda = document.getElementById("demanda").value;
    var provedor = document.getElementById("provedor").value;

    document.getElementById("example").innerHTML = "Exemplo de e-mail: <br><br>" + 
    "Assunto: [CDNTV #" + demanda + "] - " + provedor + " - Instalação <br><br>" +
    "De: seuemail@email.com <br>" + "Para: " + email + "<br><br>" +
    "Olá, tudo bem? <br><br>" +
    "Informamos que a CDNTV (Origin/Edge) foi instalada com sucesso na sua estrutura. Já é possível acessar o centro de gerenciamento" +
    "da CDNTV (CDNTV Manager) através dos acessos abaixo mencionados. Através desta central é possível: gerenciar canais, usuários e firewall," +
    "além de visualizar as estatísticas de acesso. <br><br>" +
    "Foram configurados dois servidores para sua CDNTV: <br><br>" +
    "Origin - Responsável pela gerência da CDNTV e pela recepção dos fluxos. <br>" +
    "Edge - Responsável pelo player web e pela distribuição dos fluxos. <br><br>" +
    "-- <br><br>" +
    "Origin: " + origin + "<br><br>" +
    "Usuário: admin <br>" +
    "Senha: "+ senha +" <br><br>" +
    "-- <br><br>" +
    "Edge : " + edge +" <br><br>" +
    "Usuário: cliente <br>" +
    "Senha: cliente <br><br>" +
    "-- <br><br>" +
    "Terminada a instalação dos servidores, já enviamos as imagens para a geração das aplicações. <br><br>" +
    "Em adição, você pode conferir nossa documentação completa para o uso da plataforma clicando aqui. <br><br>" +
    "No menu “Guias e Processos” encontram-se os tutoriais do passo-a-passo inicial (Começando) e da administração" +
    "da interface web (Painel de Administração), contendo vídeos explicativos para o uso de todas as funções disponíveis" +
    "na plataforma. <br><br> -- <br><br>" +
    "O nosso suporte via Skype funciona de segunda à sexta, das 08:30 às 23:00, e aos sábados, das 09:00 às 17:30 (horário de Brasília)." + 
    "Para suporte relacionado a problemas ou alguma emergência, possuímos o número plantão - (51) 98353 0000, que funciona 24 horas, todos os dias. <br><br>" +
    "Atenciosamente,"
});

document.getElementById("demanda").addEventListener("keyup", function() {
    var origin = document.getElementById("origin").value;
    var senha = document.getElementById("senha").value;
    var edge = document.getElementById("edge").value;
    var email = document.getElementById("email").value;
    var demanda = this.value;
    var provedor = document.getElementById("provedor").value;
    
    document.getElementById("example").innerHTML = "Exemplo de e-mail: <br><br>" + 
    "Assunto: [CDNTV #" + demanda + "] - " + provedor + " - Instalação <br><br>" +
    "De: seuemail@email.com <br>" + "Para: " + email + "<br><br>" +
    "Olá, tudo bem? <br><br>" +
    "Informamos que a CDNTV (Origin/Edge) foi instalada com sucesso na sua estrutura. Já é possível acessar o centro de gerenciamento" +
    "da CDNTV (CDNTV Manager) através dos acessos abaixo mencionados. Através desta central é possível: gerenciar canais, usuários e firewall," +
    "além de visualizar as estatísticas de acesso. <br><br>" +
    "Foram configurados dois servidores para sua CDNTV: <br><br>" +
    "Origin - Responsável pela gerência da CDNTV e pela recepção dos fluxos. <br>" +
    "Edge - Responsável pelo player web e pela distribuição dos fluxos. <br><br>" +
    "-- <br><br>" +
    "Origin: " + origin + "<br><br>" +
    "Usuário: admin <br>" +
    "Senha: "+ senha +" <br><br>" +
    "-- <br><br>" +
    "Edge : " + edge +" <br><br>" +
    "Usuário: cliente <br>" +
    "Senha: cliente <br><br>" +
    "-- <br><br>" +
    "Terminada a instalação dos servidores, já enviamos as imagens para a geração das aplicações. <br><br>" +
    "Em adição, você pode conferir nossa documentação completa para o uso da plataforma clicando aqui. <br><br>" +
    "No menu “Guias e Processos” encontram-se os tutoriais do passo-a-passo inicial (Começando) e da administração" +
    "da interface web (Painel de Administração), contendo vídeos explicativos para o uso de todas as funções disponíveis" +
    "na plataforma. <br><br> -- <br><br>" +
    "O nosso suporte via Skype funciona de segunda à sexta, das 08:30 às 23:00, e aos sábados, das 09:00 às 17:30 (horário de Brasília)." + 
    "Para suporte relacionado a problemas ou alguma emergência, possuímos o número plantão - (51) 98353 0000, que funciona 24 horas, todos os dias. <br><br>" +
    "Atenciosamente,"
});

document.getElementById("provedor").addEventListener("keyup", function() {
    var origin = document.getElementById("origin").value;
    var senha = document.getElementById("senha").value;
    var edge = document.getElementById("edge").value;
    var email = document.getElementById("email").value;
    var demanda = document.getElementById("demanda").value
    var provedor = this.value;

    document.getElementById("example").innerHTML = "Exemplo de e-mail: <br><br>" + 
    "Assunto: [CDNTV #" + demanda + "] - " + provedor + " - Instalação <br><br>" +
    "De: seuemail@email.com <br>" + "Para: " + email + "<br><br>" +
    "Olá, tudo bem? <br><br>" +
    "Informamos que a CDNTV (Origin/Edge) foi instalada com sucesso na sua estrutura. Já é possível acessar o centro de gerenciamento" +
    "da CDNTV (CDNTV Manager) através dos acessos abaixo mencionados. Através desta central é possível: gerenciar canais, usuários e firewall," +
    "além de visualizar as estatísticas de acesso. <br><br>" +
    "Foram configurados dois servidores para sua CDNTV: <br><br>" +
    "Origin - Responsável pela gerência da CDNTV e pela recepção dos fluxos. <br>" +
    "Edge - Responsável pelo player web e pela distribuição dos fluxos. <br><br>" +
    "-- <br><br>" +
    "Origin: " + origin + "<br><br>" +
    "Usuário: admin <br>" +
    "Senha: "+ senha +" <br><br>" +
    "-- <br><br>" +
    "Edge : " + edge +" <br><br>" +
    "Usuário: cliente <br>" +
    "Senha: cliente <br><br>" +
    "-- <br><br>" +
    "Terminada a instalação dos servidores, já enviamos as imagens para a geração das aplicações. <br><br>" +
    "Em adição, você pode conferir nossa documentação completa para o uso da plataforma clicando aqui. <br><br>" +
    "No menu “Guias e Processos” encontram-se os tutoriais do passo-a-passo inicial (Começando) e da administração" +
    "da interface web (Painel de Administração), contendo vídeos explicativos para o uso de todas as funções disponíveis" +
    "na plataforma. <br><br> -- <br><br>" +
    "O nosso suporte via Skype funciona de segunda à sexta, das 08:30 às 23:00, e aos sábados, das 09:00 às 17:30 (horário de Brasília)." + 
    "Para suporte relacionado a problemas ou alguma emergência, possuímos o número plantão - (51) 98353 0000, que funciona 24 horas, todos os dias. <br><br>" +
    "Atenciosamente,"
});

    // Exibe o exemplo de e-mail assim que a página é carregada     
    document.getElementById("origin").dispatchEvent(new Event("keyup"));     
    document.getElementById("senha").dispatchEvent(new Event("keyup")); 
    document.getElementById("edge").dispatchEvent(new Event("keyup"));         
    document.getElementById("email").dispatchEvent(new Event("keyup"));     
    document.getElementById("demanda").dispatchEvent(new Event("keyup"));     
    document.getElementById("provedor").dispatchEvent(new Event("keyup"));