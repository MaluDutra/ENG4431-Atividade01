# Atividade 01  

**PRINCIPAL (900XP)**
- Crie um CRUD em Python;
- A sua entidade, escolhida através da roleta, deve ser representada como um dicionário, que possuirá o id como propriedade obrigatória, e outras 5 propriedades, sendo 3 delas obrigatoriamente dos tipos: date, string e number (50XP);
- Cada tarefa será armazenada em uma posição de um array (lista) de dicionários (100XP);
- O programa deve ficar rodando "direto" no terminal esperando o comando do usuário. Dentre eles temos:
  - Listar todos as entradas existentes (50XP);
  - Acessar os dados de uma entrada específica (através do id) (100XP);
  - Registrar uma nova entrada (100XP);
  - Atualizar uma entrada existente (através do id) (100XP);
  - Deletar uma entrada existente (através do id) (100XP);
- Os comandos possíveis devem ser mostrados ao usuário de alguma forma (50XP);
- Todas as entradas devem vir de um arquivo TXT (50XP);
- Este arquivo deve ser atualizado a cada operação de alteração (CREATE, UPDATE e DELETE) (100XP);
- Fazer todas as validações necessárias:
  - Comando inválido (25XP);
  - Parar o programa ("quebrar" o looping) (25XP);
  - Não é possível adicionar um id já existente (ids devem ser únicos) (50XP);
  - A deleção deve ser confirmada ("Você tem certeza que deseja deletar este item?") (50XP);
  - Id inexistente (50XP).

**EXTRA (400XP)**
- Utilizar classes do Python para representar a tarefa (100XP);
- Cada uma das ações do CRUD (registro, leitura, atualização e deleção de uma tarefa) deve ter um método dentro da classe ou em uma função separada (200XP);
- Implementar um comando que busca um dado específico em uma página (EASTER EGG) (100XP). ||beautiful soup: https://www.giulianaflores.com.br/tipos-de-flores/d1138/

################################################################################
**PRINCIPAL (900XP)**
- Crie um programa em Python que permitirá ao usuário criar sua própria Flores;
- Uma tarefa deve ser representada como um dicionário, que possuirá as seguintes propriedades (50XP): #6 propriedades do tema que pegou, uma com texto e outra com valor numérico pelo menos
  - Identificador (id); #numérico ou texto -> valores sequenciais com a inserção
  - Título;
  - Descrição;
  - Status (feito ou não);
  - Data de Entrega;
- Cada registro será armazenada em uma posição de um array (lista) de dicionários (100XP); 
- O programa deve ficar rodando "direto" no terminal esperando o comando do usuário. Dentre eles temos: #deve ter opção para sair do programa
  - Listar todas as tarefas (50XP);
  - Acessar os dados de uma tarefa específica (através do id) (100XP);
  - Registrar uma nova tarefa (100XP);
  - Atualizar uma tarefa (através do id) (100XP);
  - Deletar uma tarefa (através do id) (100XP);
- Os comandos possíveis devem ser mostrados ao usuário de alguma forma (50XP);
- Todas tarefas devem vir de um arquivo TXT (50XP);
- Este arquivo deve ser atualizado a cada operação de alteração (CREATE, UPDATE e DELETE) (100XP);
- Fazer todas as validações necessárias:
  - Comando inválido (25XP);
  - Parar o programa ("quebrar" o looping) (25XP);
  - Não é possível adicionar um id já existente (ids devem ser únicos) (50XP);
  - A deleção deve ser confirmada ("Você tem certeza que deseja deletar este item?") (50XP);
  - Id inexistente (50XP). #acessar, atualizar e deletar

**EXTRA (400XP)**
- Utilizar classes do Python para representar a tarefa (100XP); #em vez de usar dicionário
- Cada uma das ações do CRUD (registro, leitura, atualização e deleção de uma tarefa) deve ter um método dentro da classe ou em uma função separada (200XP);
- Implementar um comando que busca um dado específico em uma página (EASTER EGG) (100XP).