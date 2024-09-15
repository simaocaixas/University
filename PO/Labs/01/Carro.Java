
/*
 * Um carro tem sempre uma marca, quilometragem, velocidade máxima e quatro pneus. Quando o carro é criado a sua quilometragem é igual 0 e é necessário indicar a marca, a velocidade máxima e os pneus do novo carro.
 *  O carro deve ficar sempre com a marca indicada. É possível saber a quilometragem do carro, a sua marca e se algum dos seus pneus está vazio.
 *  A marca é representada simplesmente por uma cadeia de caracteres. É possível também alterar o valor da quilometragem do carro. Um carro pode estar em movimento ou parado. Se estiver em movimento, então terá uma dada velocidade. 
 * Um carro pode ainda estar travado, Se o carro estiver travado, então não se movimentará. Um carro quando é criado está sempre travado. É possível travar ou destravar um carro.
 *  É ainda possível alterar a velocidade do carro desde que o carro não esteja travado. Não é possível ultrapassar a velocidade máxima do carro.
 * 
 * 
 */


 public class Carro {

    private final String _marca;       // Sempre a mesma marca = Constante 
    private int _quilometragem;
    private int _velocidade;
    private int _velocidadeMaxima;
    private Pneu[] _pneus;             // Classe realizada no 01
    private boolean _travado;

    public Carro(String marca, int velocidadeMaxima, Pneu[] pneus) {

      _marca = marca;
      _velocidadeMaxima = velocidadeMaxima;
      _pneus = pneus;                  // Assumindo que pneus é **sempre uma lista com quatro pneus  
      _quilometragem = 0;
      this.travar()
    }

    public int quilometragem() {
      return _quilometragem;
    }

    public String marca() {
      return _marca;
    }

    public boolean vazio() {
      for (Pneu pneu : _pneus) {
        if (pneu.vazio()) {
          return true;
        }
      }
        return false;
    }

    public void alteraQuilometragem(int novaQuilometragem) {
      _quilometragem = novaQuilometragem;
    }

    public void travar() {
      _travado = true;
      _velocidade = 0;
    }

    public void destravar() {
      _travado = false;
    }

    public void mover(int velocidade) {
      if (!_travado) {
        if (velocidade <= velocidadeMaxima) {
          _velocidade = velocidade;
        } 
      }

    }

 }
