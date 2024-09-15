/* 
 * Considere o seguinte domínio de aplicação:
 * Um pneu tem uma dada pressão de ar. Cada pneu tem também uma pressão de ar recomendada. 
 * Um pneu quando é criado tem uma dada pressão de ar e sabe também a sua pressão de ar recomendada. 
 * Pode-se saber a pressão de ar  e a pressão recomendada de um dado pneu. Não deve ser possível alterar a pressão de ar recomendada de um pneu.
 * É possível saber se um pneu está vazio ou não. O pneu está vazio caso a sua pressão de ar seja inferior a 80% da pressão de ar recomendada. 
 * É possível alterar a pressão de ar de um pneu. Se o pneu passar a ter uma pressão de ar superior a 150% da pressão de ar recomendada, então o pneu estoira (fica com um furo) e fica com uma pressão de ar igual a 0. 
 * Quando um pneu tem um furo já não é possível alterar a sua pressão. É possível saber se um pneu tem um furo ou não.
 * Primeiro modele o este domínio e depois concretize-o.Compare a sua solução com a solução proposta pelo corpo docente: Pneu.java
*/

/*
+-------------------------------------------+
|Pneu                                       |
+-------------------------------------------+
| pressaoAr:int                             |
| pressaoArRecomendada:int                  |
| furado:boolean                            |
+-------------------------------------------+
| Pneu(pressao:int, recomendada:int)        |
| alterarPressao(novaPressao:int):void      |
| obtemPressaoAr(): int                     |
| obtemPressaoArRecomendada(): int          |
| estaVazio(): boolean                      |
| estaFurado(): boolean                     |
+-------------------------------------------+
*/


public class Pneu {

          private int _pressaoDeAr;
          private int _pressaoDeArRec;
          private boolean _furo = false;         // inicialização por omissão           

          public Pneu(int pressaoDeAr, int pressaoDeArRec) {

                    _pressaoDeAr = pressaoDeAr;
                    _pressaoDeArRec = pressaoDeArRec;
          }

          public int pressaoDeAr() {
                    return _pressaoDeAr;
          } 
          public int pressaoDeArRec() {
                    return _pressaoDeArRec;
          }          

          public boolean furo() {
                    return _furo;
          }

          public boolean vazio() {
                    return (_pressaoDeAr < _pressaoDeArRec * 0.8);
          }
          
          public void encher(int pressao) {
                    if (!_furo) {
                              _pressaoDeAr += pressao;
                              if (_pressaoDeAr > _pressaoDeArRec * 1.5) {
                                        _furo = true;
                                        _pressaoDeAr = 0;
                              }
                    }
          }

}
