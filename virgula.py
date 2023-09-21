import toml


def carregar_usuarios():
    try:
        with open(".streamlit/config.toml", "r", encoding="latin-1") as f:
            dados = toml.load(f)
            return dados.get("users", {})
    except FileNotFoundError:
        return {}


def cadastrar_usuario(usuario, senha, cidade):
    usuarios = carregar_usuarios()
    senhas = usuarios.items()

    if usuario in usuarios:
        print("Usuário já existe!")
        return

    novo_usuario = {usuario: {"senha": senha, "cidade": cidade}}
    usuarios.update(novo_usuario)

    # Salva as informações atualizadas no arquivo config.toml
    with open(".streamlit/config.toml", "w", encoding="latin-1") as f:
        toml.dump({"users": usuarios}, f)


def main():
    pass
    # usuario = input("Digite o nome de usuário: ")
    # senha = input("Digite a senha: ")
    # cidade = input("Digite a cidade: ")

    # cadastrar_usuario(usuario, senha, cidade)


def imprimir_usuarios():
    usuarios = carregar_usuarios()

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for usuario, dados in usuarios.items():
        senha = dados.get("senha")
        cidade = dados.get("cidade")
        print(f"Usuário: {usuario}, Senha: {senha}, Cidade: {cidade}")


if __name__ == "__main__":
    main()
    imprimir_usuarios()
    cadastrar_usuario("teste", "teste", "teste")
