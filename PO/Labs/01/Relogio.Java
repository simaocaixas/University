/* Um Relógio tem as propriedades de hora (em formato de 24 horas: hora, minuto e segundo), além de um alarme que pode ser ativado ou desativado, com hora e minuto configuráveis.
* A funcionalidade do relógio inclui inicializá-lo com a hora atual, ajustar a hora, minuto e segundo, ativar e desativar o alarme, ajustar a hora e minuto do alarme, exibir a hora atual no formato de 24 horas
* e verificar se o alarme deve tocar, ou seja, se a hora atual coincide com a hora do alarme quando o alarme está ativado.
*/

public class Relogio {
	
	private int _hora;
	private int _minuto;
	private int _segundo;

	private boolean _alarme = false;

	private int _alarmeHora;
	private int _alarmeMinuto;
	

	public Relogio(int hora, int minuto, int segundo) {

		_hora = hora;
		_minuto = minuto;
		_segundo = segundo;

	}

	public void relogioAjustar(int hora, int minuto, int segundo) {

		_hora = hora;
		_minuto = minuto;
		_segundo = segundo;
	} 

	public void alarmeAjustar(int hora, int minuto) {

		_alarmeHora = hora;
		_alarmeMinuto = minuto;
	
	}

	public void ativarAlarme() {
		_alarme = true;
	}

	public void desativarAlarme() {
		_alarme = false;
	}

	public void exibir() {

		System.out.println("..............");
		System.out.printf("%02d:%02d:%02d\n", _hora, _minuto, _segundo);
		
	}

    public boolean deveTocar() {
        return _alarme && _hora == _alarmeHora && _minuto == _alarmeMinuto;
    }
}


