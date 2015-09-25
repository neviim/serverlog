Script para ser usado no gron.

Armazena por 48 horas os log de algumas variáveis do sistema
(memoria, disco, processador), a cada 5 minutos é gerado um
registro de 2k.



# Configurar

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