public class Numero {

    private int _valor; // Inicializado por omissão para 0

    public Numero(int valor) {
        _valor = valor;
    }

    public int obterValor() {
        return _valor;
    }

    public void alteraValor(int v) {
        _valor = v;
    }

    public String obterString() { 
        return Integer.toString(_valor);
    }

    public boolean saoIguais(Numero n) {
        return _valor == n.obterValor(); 
    }

    public Numero maior(Numero n) {
        if (_valor > n.obterValor()) {
            return this;
        } else {
            return n;
        }
    }
}
