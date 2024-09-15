/*
 *  Uma caneta tem uma dada capacidade de tinta, cor e uma marca. A caneta mantém ainda a quantidade de tinta que tem. Quando se cria uma caneta é necessário indicar a sua marca, capacidade de tinta e cor.
 *  Uma caneta quando é criada está sempre cheia. A marca e a cor são representadas por uma cadeia de caracteres. Uma caneta pode escrever, ser recarregada e indicar a sua cor e quantidade de tinta ainda disponível.
 *  A operação de escrever recebe a cadeia de caracteres a escrever no terminal. Esta cadeia de caracteres só é escrita caso a caneta ainda tenha tinta (não interessa a quantidade).
 *  Escrever uma cadeia de caracteres gasta uma quantidade de tinta igual ao número de caracteres a escrever (o método length() de String devolve o número de caracteres da cadeia de caracteres). 
 *  Atenção que a quantidade de tinta não pode ficar um número negativo. A operação de recarregar recebe com a argumento a quantidade tinta a adicionar e deve ter em conta a capacidade da caneta. 
 *  Deve devolver a quantidade de tinta não utilizada no carregamento.
 * 
 *  Acrescente agora uma nova funcionalidade que permite recarregar a caneta com tinta de uma determinada cor.
 *  O recarregamento ocorre com a funcionalidade descrita anteriormente se a cor da tinta a colocar for igual à cor da caneta, devolvendo neste caso a quantidade de tinta não utilizada.
 * 
 * Acrescente um novo método que permite verificar se duas canetas são iguais ou não de acordo com a seguinte semântica: duas canetas são iguais se tiverem a mesma marca, cor e capacidade.
 * 
 * 
 */

 public class Caneta {

  private int _capacidade;
  private int _tinta;
  private String _marca;
  private String _cor;

  public Caneta(int capacidade, String marca, String cor) {
      _capacidade = capacidade;
      _tinta = capacidade;            // Caneta começa cheia
      _marca = marca;
      _cor = cor;
  }

  public int escrever(String texto) {
      int quantidadeNecessaria = texto.length();
      if (quantidadeNecessaria <= _tinta) {
          System.out.println(texto);
          _tinta -= quantidadeNecessaria;
          return quantidadeNecessaria;
      }
      return -1;
  }

  public int recarrega(int tinta) {
      int tintaDisponivel = Math.min(tinta, _capacidade - _tinta);
      _tinta += tintaDisponivel;
      return tinta - tintaDisponivel;
  }

  public int recarrega(int tinta, String cor) {
    if (cor.equals(_cor)) {
        return recarrega(tinta);             
    } else {
        return -1;
    }
}

public boolean iguais(Caneta c) {
  if (c == null) {
      return false; 
  }
  return _cor.equals(c.cor()) && _marca.equals(c.marca()) && _capacidade == c.capacidade();
}


  public int capacidade() {
      return _capacidade;
  }

  public String marca() {
      return _marca;
  }

  public String cor() {
      return _cor;
  }
}
