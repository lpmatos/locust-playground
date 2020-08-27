# Demo Bookinfo

## Visão geral

Neste tutorial, você usa o aplicativo Bookinfo, que é um aplicativo de microsserviços poliglota de quatro camadas, que mostra informações sobre livros. Esse aplicativo foi desenvolvido para ser executado no Kubernetes, mas primeiro é preciso implantá-lo em uma instância do Compute Engine usando o Docker e o Docker Compose. Com o Docker Compose, você descreve apps de vários contêineres por meio de descritores YAML. Depois, é possível iniciar o app executando um único comando.

Temos as seguintes aplicações:

* **ProductPage**: 
  * O ProductPage é uma aplicação em Python que será o nosso frontend. 
  * Ela receberá as requisições dos clientes e fará as chamadas para os demais microserviços via endpoint.
* **Reviews**: 
  * Existem 3 releases rodando v1, v2, v3 do nosso service Reviews, que foi desenvolvido em Java. 
  * O ProductPage irá chamar o microserviço Reviews, via endpoint, e o serviço Reviews vai chamar o Ratings, também via endpoint.
* **Details**: 
  * Esse microsserviço, que foi desenvolvido em Ruby, irá nos fornecer apenas detalhes estáticos dos books que não irão mudar;
* **Ratings**: 
  * Essa é uma aplicação em node que irá fornecer informações apenas para as release v2 e v3 dos serviços reviews.

Depois de entender a arquitetura do nosso ambiente, vamos agora escrever os arquivos compose file (bookinfo.yml) para deployar a nossa aplicação.
