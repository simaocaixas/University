public class Biblioteca {
    private List<Livro> livros;
    private List<Usuario> usuarios;

    public Biblioteca() {
        _livros = new ArrayList<>();
        _usuarios = new ArrayList<>();
    }

    public void adicionarLivro(Livro livro) {
        livros.add(livro);
    }

    public void removerLivro(Livro livro) {
        livros.remove(livro);
    }

    public void registrarUsuario(Usuario usuario) {
        usuarios.add(usuario);
    }

    public void removerUsuario(Usuario usuario) {
        usuarios.remove(usuario);
    }

    public void emprestarLivro(String isbn, String matricula) {
        Livro livro = encontrarLivroPorIsbn(isbn);
        Usuario usuario = encontrarUsuarioPorMatricula(matricula);
        if (livro != null && usuario != null && livro.isDisponivel()) {
            usuario.emprestarLivro(livro);
        }
    }

    public void devolverLivro(String isbn, String matricula) {
        Livro livro = encontrarLivroPorIsbn(isbn);
        Usuario usuario = encontrarUsuarioPorMatricula(matricula);
        if (livro != null && usuario != null) {
            usuario.devolverLivro(livro);
        }
    }

    private Livro encontrarLivroPorIsbn(String isbn) {
        for (Livro livro : livros) {
            if (livro.getIsbn().equals(isbn)) {
                return livro;
            }
        }
        return null;
    }

    private Usuario encontrarUsuarioPorMatricula(String matricula) {
        for (Usuario usuario : usuarios) {
            if (usuario.getMatricula().equals(matricula)) {
                return usuario;
            }
        }
        return null;
    }
}
