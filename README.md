Script para ser usado no gron.

Armazena por 48 horas os log de algumas variáveis do sistema
(memoria, disco, processador), a cada 5 minutos é gerado um
registro de 2k.


# Configurar agente

    Sugestão de que crie um diretorio em:

        sudo mkdir /usr/local/src/serverlog
        sudo cp ~/env/src/serverlog/getstatus.py /usr/local/src/serverlog


    Em arquivo crontab acresentar esta linha:

        # crontab -e

                */5 * * * *  root python /usr/local/src/serverlog/getstatus.py


    Comandos masicos do crom tab:

        crontab -e      Edita o crontab atual do usuário
        crontab -l       Exibe o atual conteúdo do crontab do usuário
        crontab -r       Remove o crontab do usuário


# Server

    Baixando este projeto:

        mkdir projeto
        cd projeto
        git clone https://github.com/neviim/serverlog.git
        cd serverlog-master/app

        python app.py

        Em seu browse entre no endereço localhost:4000
        Endereço de acesso:

                http://localhost:4000
                http://localhost:4000/ping
                http://localhost:4000/cpu

                # APIs
                lhttp://localhost:4000/api/get_cpu



# Lista de pendencias a ser desenvovido
    - Autenticação
    - API - cpu_system
    - API - cpu_idle
    - API - cpu_memoria_ficica, consumo
    - API - cpu_disco_utilizado, espaço em disco utilizado
    - Implementar alertas de indicadores
    - Linha vermelha de indicador maximo
    - Linha azul tracejada de status de media do monitoramento.
    - Melhorar Frontend
    - Instalador de pendencias
    - Acertar mnodulo de agente para tratar multi servidores.
    - Criar arquivo config





# V-0.2.0
    - Criar modulo frontend, que mostre status dos parâmetros monitorado.
    - Função de leitura no mongodb
    - Criar o server com acesso as API de search no mongoDB.
    - Configurar as bibliotecas js utilizadas no projeto.
    - Função webserver valida funcionamento do server, ping/pong
    - Método home, get_cpu, pong, cpu
    - Criar modulo JavaScript para acesso a API retornando o gráfico em tela.
    - Organizar as pastas de trabalho agentserver, static, template.
    - Documentação das atividades desenvolvidas.

# V-0.1.0
    - Definir o que sera implementado neste codigo inicial.
    - Esta versão 0.1.0, tem por finalidade testar o conseito.
    - Criar pasta no github deste projeto.
    - Considera que tenha um banco mongoDB rodando.
    - Escrever o basico, ler status desejado do sistema.
    - Criar um banco no mongoDB de nome: logserver.
    - No server que for ser monitorado colocar este escript no Cron.
      */5 * * * *  root python /path/para/script_getdados.
    - Efetuar os teste de gravação do log no server mongodb.
    - Atualizar a documentação e commit.