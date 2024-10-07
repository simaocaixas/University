## Enunciado:

public class Form {
	
	.
	.
	.
	.

	public getForm(int id) -> retorna a forma ou retorna uma execao "FormDoesntExistsExeption"

	public setId(int id) -> muda o id de uma forma

	public boolean addForm(Form form) -> adiciona form a um editor (true se adiciona false caso contrario)

}


Faz agora um metodo de Form que cria uma copia de uma forma; Recebe dois identificadores, um da forma original e um da forma nova. Podes usar o metodo clone() que copia um objeto. O metodo a criar deve lançar a exceçãEsteo "CloneErrorExeption" que é lançado se a o id da forma original nao existir ou se o identificador novo já existir. 

Faz o novo metodo e a class CloneErrorExeption

## Resposta: 

public class CloneErrorExeption extends Exeption {
	
	public CloneErrorExeption(String m) {
		super(m);
	}
}


public cloneForm(int idOriginal, int idCopia) throws CloneErrorExeption {
	
	try {
		Form novaForma = clone(getForm(int idOriginal));
		novaForma.setId(idCopia)
	} catch (FormDoesntExistsExeption) {
		throw new CloneErrorExeption("A forma não existe");
	}


	if (novaForma.addForm() == false) {
		throw new CloneErrorExeption("A forma já existe")
	}
}
