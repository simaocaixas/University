public class Usuario {
    private String nome;
    private String matricula;
    private List<Livro> livrosEmprestados;

    public Usuario(String nome, String matricula) {
        _nome = nome;
        _matricula = matricula;
        _livrosEmprestados = new ArrayList<>();
    }

    public String getNome() {
        return nome;
    }

    public String getMatricula() {
        return matricula;
    }

    public void emprestarLivro(Livro livro) {
        if (livrosEmprestados.size() < 5 && livro.isDisponivel()) {
            livrosEmprestados.add(livro);
            livro.emprestar();
        }
    }

    public void devolverLivro(Livro livro) {
        livrosEmprestados.remove(livro);
        livro.devolver();
    }
}
