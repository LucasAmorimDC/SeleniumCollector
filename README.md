# SeleniumCollector

## Descrição

    O BOT tem como sua principal característica uma configuração externa, feita dinamicamente por um arquivo JSON, cujo a função é executar cada comando escrito
    sem a necessidade de quaisquer alteração no codigo fonte.
    O coletor conta com uma interface simples, porém muito útil capaz de executar as ações uma de cada vez, permitindo que o programador tenha a praticidade para encontrar os       elementos e efetuar a coleta mais precisamente.
    A interface contém opções simples e precisas, dadas pelo "COMBOBOX" com a ideia de agilizar a escolha de ações e evitar erros de digitação.
    A ideia por traz da interface é simples, cada ação salva pela interface é escrita no arquivo externo JSON e executada em seguida pelo BOT, e além da opção "SAVE" que tem a       função de salvar e escrever o JSON foi implementado um botão DELETE, para caso de o elemento não for encontrado, ou não interagível. 

## ⚙️ Como utilizar
    
    ## ACTION
      O BOT até então conta com 5 ações diferentes, sendo elas "Digitar, Enter, Click, Double_Click, Extract, Insert".

      DIGITAR, Cuja função é digitar tudo oque estiver escrito no campo "value".
      ENTER, Cuja função e apertar a tecla "Enter" no elemento solicitado no campo "Element".
      CLICK, Cuja função é clicar no elemento solicitado no campo "Element".
      DOUBLE_CLICK, Cuja função é efetuar o duplo click no elemento solicitado no campo "Element".
      EXTRACT, Cuja função é extrair uma informação(Ex: Tabela), da tag informata no campo "Element".
         OBS: É criada uma pasta "Extract" onde guardará todos os arquivos estraídos para que fiquem prontos para
         serem inseridos no banco.
      INSERT, Cuja função é inserir os arquivos extraídos para a pasta "Extract" diretamente para o banco de dados SQL.
         OBS: É necessario efetuar a criação das tabelas com suas respectivas colunas antes de efetuar a inserção dos dados.
      
    ## FIND
      O BOT até então e capaz de interagir com 5 elementos HTML, sendo eles "TAG_NAME, CLASS_NAME, CSS_SELECTO, ID, XPATH", capazes de guardar em variáveis o elemento                 selecionado e interagir com o mesmo.
      
    ## SLEEP
      SPIN, Campo que conta com uma numeração de 1 a 5, com a função de fazer o código esperar os segundos selecionados antes de efetuar a ação.
    
    ## ELEMENT
      Campo reservado para o preenchimento do elemento coletado do HTML da página que será feita a coleta.
      
    ## VALUE
      Campo reservado para o preenchimento do valor que será Digitado pela "ACTION" "Digitar".
    
    ## SAVE
      Botão cuja função e salvar todas as ações dadas nos campos anteriores e escrever no JSON para serem executadas pelo BOT.
    
    ## DELETE
      Botão Cuja função é deletar a ultima ação escrita no JSON.
    
    ## OUTPUT
      Campo revervado para imprimir todos os passos efetuados para melhor viabilidade ao decorrer da programação.


### 📋 Pré-requisitos

    O coletor conta com os arquivos externos Steps.json, config.ini, Chromedriver.exe que são essenciais para execução do programa.
    
    ## Steps.json
      Arquivo necessário para execução das ações.
     
    ## config.ini
      Arquivo responsável por guardar os dados do usuário como:
        [DADOS]
        user = --nome de usuário utilizado para login na plataforma.
        password = --senha utilizada para login na plataforma.

        [PLATFORM]
        url = --url do site que deseja acessar.

        [CONTENT] -- Dados a serem preenchidos do HTML do site
        tag = --tag do HTML que deseja extrair algo.

        [SQL] -- Dados a serem preenchidos do banco de dados SQL
        database = --nome do banco de dados
        table = --nome da tabela
        server = --nome do servidor
        user = --nome de usuario
        pass = --senha
        
     ## Chromedriver.exe
        Essencial para a funcionalidade do coletor, não esqueça de manter sempre atualizado.

