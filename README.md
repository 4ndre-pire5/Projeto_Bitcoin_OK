Projeto disciplina DataEngineering & DataScience.

Realizado por André Pires e Gabriel Henrique.

- A aplicação faz a ingestão de dados históricos do BITCOIN utilizando a API CoinAPI.io (https://docs.coinapi.io/).

- Existem outras API´s que poderiam ser utilizadas, porém a maioria delas só disponibiliza dados históricos através de assinaturas pagas de planos. A CoinAPI.io foi a primeira encontrada que disponibiliza os dados históricos em plano free, porém com limite de 100 consultas, sendo assim, para conseguir os dados foi utilizado o período mensal de consulta para evitar o estouro do limite.

- Para solicitar os dados, é necessário efetuar cadastro no sistema, onde será gerada uma chave (api_key) que deverá ser informada no código para obter acesso às informações.

- Através dessa API é possível obter dados de diversas moedas digitais em diferentes períodos. A página web da API disponibiliza uma documentação extremamente útil, explicando como fazer as diferentes solicitações com exemplos de utilização em diferentes linguagens de programação.

- A aplicação foi criada em PYTHON, seguindo exemplos que existem na documentação da API. A escolha pela utilização da linguagem PYTHON foi feita com intuito de conhecer melhor a linguagem em si e todas as ferramentas que ela fornece, desde a requisição dos dados, até a criação e armazenamento desses dados em um banco de dados e também o tratamento dos dados para criação dos gráficos que a aplicação vai gerar.

- Os dados são fornecidos pela API em formato JSON e a aplicação faz toda a implementação(criação do banco de dados, conexão com o banco de dados, criação da tabela e inserção de dados na tabela)para uso com o MySQL.

- Foi criado um banco de dados chamado "COINAPI" com duas tabelas, a primeira nomeada como "CRYPTO_PRICES" que vai armazenar os dados de 5 anos do valor do BITCOIN em intervalos mensais, fornecendo 68 linhas de informção . A segunda tabela  nomeada como "CANDLE_DATAS" vai armazenar os últimos dados diários do valor do BITCOIN fornecendo 100 linhas de informação, que vai cobrir aproximadamente os últimos 4 meses.

- A aplicação vai gerar dois gráficos, o primeiro vai ilustrar o valor mensal médio dos últimos 5 anos do BITCOIN. Para extrair as informações necessárias para a construção do gráfico, foi utilizada a ferramenta "pandas", de onde foi criado um dataframe com os valores desejados e a inclusão de uma nova coluna com o valor médio calculado para criação do gráfico, e a ferramenta  "matplotlib" que auxilia a criação do gráfico.

- O segundo gráfico criado é do tipo "candlestick", muito utilizado em sistemas financeiros. Esse gráfico vai gerar informações dos últimos 30 dias dos valores (valor de abertura, fechamento, maior e menor valor) do BITCOIN. A extração desses dados também foi feita com auxílio do "pandas" e para gerar o gráfico foi utilizada a ferramenta "mplfinace".

- Dentro da pasta "DEPLOY", existe um arquivo nomeado "main.exe" que é um executável do projeto. Porém esse executável foi feito em cima de uma versão com o gráfico candle referente ao mês de julho/23. O gráfico referente ao mês de agosto/23 é gerando rodando a aplicação diretamente no console.

- O desenvolvimento da aplicação exigiu um grande trabalho de pesquisa para encontar a API ideal para obtenção dos dados, conhecer melhor a linguagem PYTHON, o MySQL,  e como utilizar as ferramentas que auxiliaram na criação dos dataframes e dos gráficos.

- A aplicação oferece uma grande ajuda para entusiastas do mercado de cripto moedas, profissionais do mercado e até mesmo empresas, que desejam obter informações variadas sobre a cripto moeda desejada.

- Diversas melhorias podem ser feitas na aplicação, desde a utilização de um framework, até melhoria no armazenamento e tratamento dos dados.