import streamlit as st
from st_pages import show_pages_from_config
import toml
# Either this or add_indentation() MUST be called on each page in your
# app to add indendation in the sidebar

show_pages_from_config()


# Função para criar ou atualizar o arquivo .toml com as informações de usuário e senha
def carregar_usuarios():
    try:
        with open(".streamlit/config.toml", "r", encoding="latin-1") as f:
            dados = toml.load(f)
            return dados.get("users", {})
    except FileNotFoundError:
        return {}


def verifica_cadastro(usuario,senha, cidade):
    usuarios = carregar_usuarios()
    print(usuarios)
    if usuarios.get(usuario) == usuario and usuarios.get(senha) == senha and usuarios.get(cidade) == cidade:
        return True

def cadastrar_usuario(usuario, senha, cidade):
    usuarios = carregar_usuarios()
    novo_usuario = {usuario: {"senha": senha, "cidade": cidade}}
    usuarios.update(novo_usuario)

    # Salva as informações atualizadas no arquivo config.toml
    with open(".streamlit/config.toml", "w", encoding="latin-1") as f:
        toml.dump({"users": usuarios}, f)
    
def main():
    st.title("📝 - Cadastro de Usuarios")
    
    container = st.container()
    
    # cidade = container.radio("Escolha uma opção", ["Ouro Preto", "Ji-Parana"])

    usuario = container.text_input("Usuario")
    senha = container.text_input("Senha", type='password')
    cidade = container.text_input("Cidade")

    if container.button("Cadastrar"):
        if verifica_cadastro(usuario, senha, cidade):
            st.error("Usuario já cadastrado")
        else:
            cadastrar_usuario(usuario, senha, cidade)
            st.success("Usuario cadastrado com sucesso!")
            

    
if __name__ == "__main__":
    main()

