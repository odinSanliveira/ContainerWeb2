
## Atividade

Adicione uma novo microsserviço a arquitetura atual do exemplo. Ele será responsável pelo novo *endpoint* da api que realiza uma multiplicação (**/mult**). Ele receberá dois valores **op1**, **op2** e retornará o resultado da multiplicação. Você precisa criar umaa nova aplicação coma uma outra framework (não utilizar flask).

Devido a sua alta demanda de acesso, o microsserviço precisa ser replicada com 3 containers. A distribuição será feita através da política de balanceamento de carga *Round Robin* com diferentes pesos e funções. Um container deve ser configurado como **backup** e os outros dois com o peso 3 e 1, respectivamente. Para mais informações sobre distribuição de peso, acesse: https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/ (*Seção Server Weights*).

Reponda as seguintes perguntas abaixo após desenvolver as modificações necessárias para que esses novos requisitos sejam alcançados. 

1. Como é feita a distribuição das requisições para o endpoint **/mult** ? Discorra o que acontece. (use Postman, Isomnia, thunder client...)

2. O que acontece quando os containers da aplicação **mult** param de funcionar? 
Para simular esse cenário [use o *docker stop nome_container* para parar containers](https://medium.com/xp-inc/principais-comandos-docker-f9b02e6944cd). Pare cada um dos containers que estão recebendo requisição da aplicação **mult** por vez e analise o que está acontecendo. 
> O container de **backup** não deve ser parado. 

Ao terminar os experimentos, lembre-se de executar ```docker-compose down```
