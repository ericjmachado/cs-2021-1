# Tarefa 016 - Tratamento de Erros - 10/09/2021

1. Criar uma classe chamada **Contato**, que deverá ter os seguintes atributos:
   * nome, do tipo String;
   * Telefone, do tipo Integer;
   * Email, do tipo String;
2. Crie uma classe de Exceção chamada **ContatoNaoEncontratoException**, conforme exemplificado na aula online.
   * A mensagem constante de uma exceção desta classe deverá ser: "Contato não encontrado!"
3. Criar uma classe chamada **Agenda**, que deverá ter:
   * Uma lista de contatos;
   * Um método para adicionar contato;
   * Um método para remover contato;
   * Um método para pesquisar contato pelo nome. Este método deverá disparar (lançar) uma exceção do tipo ContatoNaoEncontratoException.
4. Crie uma classe de **AgendaTeste**. Nesta classe:
   * Adicione 3 contatos à agenda;
   * Consulte um contato, tratando a exceção disparada pelo método de consulta. Imprimindo a mensagem de erro e a pilha de exceção.
   * Na cláusula **finally**, remova todos os contatos da agenda;
5. Considere o seguinte código, escrito na Linguagem de Programação Java:

~~~java
import java.util.Scanner;

public class Divisao {

    private static Scanner sc = new Scanner(System.in);

    public static int divide(int dividendo, int divisor){
        return dividendo/divisor;
    }

    public static void main (String args[]) {

        System.out.println("Informe o valor do dividendo: ");
        int dividendo = sc.nextInt();
        System.out.println("Informe o valor do divisor: ");
        int divisor = sc.nextInt();
        System.out.println(divide(dividendo, divisor));
    }

}
~~~
  4.1 Altere o método divide() para disparar "explicitamente" (usando os comandos _throws_ e _throw_) uma exceção do tipo _ArithmeticException_;
  4.2 Altere o método main para fazer o tratamento da exceção disparada. Neste tratamento deverá imprimir a mensagem de erro e a pilha de exceção.

**INSTRUÇÕES**
1. Você pode resolver estes exercícios na linguagem de programação da sua preferência.
2. Na _branch_ aluno, do seu repositório pessoal, criar a pasta **tarefa016**.
3. _Commitar_ nesta pasta somente os arquivos fonte ".java, .py, .js, .cs" gerados para a resolução dos exercícios.
4. O prazo para entrega desta tarefa é as 23h59min do dia 10/09/2021.