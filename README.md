# Gestor de Contactos
Este é um simples gestor de contactos em Python que permite adicionar, editar, remover e pesquisar contactos num ficheiro de texto. A aplicação também permite listar todos os contactos existentes no ficheiro.

## Funcionalidades
**Adicionar Contacto:** Adiciona um novo contacto ao ficheiro.

**Editar Contacto:** Edita o nome e/ou número de um contacto existente.

**Remover Contacto:** Remove um contacto do ficheiro.

**Pesquisar Contacto por Nome:** Pesquisa um contacto pelo nome.

**Pesquisar Contacto por Número:** Pesquisa um contacto pelo número.

**Listar Contactos:** Lista todos os contactos do ficheiro.


**Sair:** Sai da aplicação.

## Começando

### Para rodar o programa deves executar o seguinte comando:
```
python main.py
```

### Após isso aparecerá o menu para escolheres a funcionalidade:
Para escolheres é só introduzir o número a frente da funcionalidade.
```
1. Adicionar Contacto
2. Editar Contacto
3. Remover Contacto
4. Pesquisar Contacto por Nome
5. Pesquisar Contacto por Numero
6. Listar Contactos
7. Sair
```

#### *Adicionar Contacto:*
Para adicionar um contacto deves preencher os seguintes parametros:
```
Nome,Numero,Email,Endereço
```

#### 1º *Editar Contacto:*
É só introduzir o nome do contacto a ser edita e executar as edições.

#### 2º *Remover Contacto:*
Colocar o nome do contacto a ser removido.

#### 3º *Pesquisar Contacto por Nome:*
Introduzir o nome do contacto que queres pesquisar e ja está.

#### 4º *Pesquisar Contacto por Número:*
É o mesmo que pesquisar por nome mas só que em vez do nome introduzes o número do contacto.

#### 5º *Listar Contactos:*
Faz a listagem de todos os contactos presentes no ficheiro.

#### 6º *Sair:*
Como o nome já diz esta funcionalidade é para terminar o programa.

## Estrutura dos Ficheiros
**contacts.py:** Contém as funções para manipulação dos contactos *(adicionar, editar, remover, pesquisar e listar)*.

**main.py:** Contém a interface de linha de comando para interagir com o utilizador.

## Formato do Ficheiro de Contactos

Os contactos são armazenados num ficheiro de texto chamado **contacts.txt**, com cada linha representando um contacto no seguinte formato: ***Nome, Numero, Email, Endereço***.