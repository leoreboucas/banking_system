<h1>Sistema Bancário</h1>

<h2>
    Desafio de projeto proposto pelo bootcamp Python AI Backend Developer
</h2>

<h3>Proposta</h3>

<p>
    Desenvolver uma aplicação de um sistema bancário que tem apenas 3 operações: depositar, sacar e verificar o extrato.
</p>

<h3>Regras</h3>

<h4>Operação de Depósito:</h4>

<p>
    Deve ser possível depositar valores positivos para  a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número de agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
</p>

<h4>Operação de Saque:</h4>

<p>
    O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
</p>

<h4>Operação de Extrato:</h4>

<p>
    Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
</p>
<p>
    Os valores devem ser exibidos utilizando o formato R$ xxx.xx, por exemplo:
</p>
<p>1500.45 = R$ 1500.45</p>