import java.util.ArrayList;
import java.util.List;

public class NumeroComMemoria extends Numero {
    
    private List<Integer> numeros = new ArrayList<>();
    private boolean _desfazer = false;
    private int _index = -1;

    @Override
    public int obterValor() {
        return numeros.get(_index);
    }
    
    public NumeroComMemoria(int valor) {
        super(valor);
        numeros.add(valor);
        _index += 1;
        
    }

    public void alteraValor(int v) {
        numeros.add(v);
        _index += 1;
    }

    public void desfazer() {

        if (!_desfazer) {
            _index -= 1;
            _desfazer = true;
        } else {
            _index += 1;
            _desfazer = false;
        }
    }

    public int valorAnterior() { 
        if (_index <= 0) {
            return numeros.get(_index);
        } else {
            return numeros.get(_index - 1); 
        }
    }

}

