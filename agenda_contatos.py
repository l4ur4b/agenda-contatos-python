import json
import os

class Contato:
    def __init__(self, nome, telefone, email=""):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def to_dict(self):
        # converte o objeto para dicionário (para salvar em JSON)
        return {
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email
        }

    def __str__(self):
        return f"{self.nome} | {self.telefone} | {self.email}"


class Agenda:
    def __init__(self, arquivo="contatos.json"):
        self.arquivo = arquivo
        self.contatos = []
        self.carregar()  # carrega automaticamente ao iniciar

    def carregar(self):
        # lê o arquivo JSON se ele existir
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.contatos = [
                    Contato(c["nome"], c["telefone"], c["email"])
                    for c in dados
                ]

    def salvar(self):
        # persiste todos os contatos no arquivo JSON
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(
                [c.to_dict() for c in self.contatos],
                f, indent=2, ensure_ascii=False
            )

    def adicionar(self, nome, telefone, email=""):
        contato = Contato(nome, telefone, email)
        self.contatos.append(contato)
        self.salvar()  # salva sempre que adicionar
        print(f"Contato '{nome}' adicionado!")

    def buscar(self, termo):
        # busca parcial — não precisa digitar o nome completo
        termo = termo.lower()
        resultados = [
            c for c in self.contatos
            if termo in c.nome.lower() or termo in c.email.lower()
        ]
        return resultados

    def remover(self, nome):
        antes = len(self.contatos)
        self.contatos = [c for c in self.contatos if c.nome.lower() != nome.lower()]
        if len(self.contatos) < antes:
            self.salvar()
            print(f"Contato '{nome}' removido.")
        else:
            print("Contato não encontrado.")

    def listar(self):
        if not self.contatos:
            print("Agenda vazia.")
            return
        for i, c in enumerate(self.contatos, 1):
            print(f"{i}. {c}")


# --- uso básico para testar ---
if __name__ == "__main__":
    agenda = Agenda()

    agenda.adicionar("Laura", "11 91234-5678", "laura@email.com")
    agenda.adicionar("Carlos", "11 99876-5432")

    print("\n--- todos os contatos ---")
    agenda.listar()

    print("\n--- busca por 'lau' ---")
    for c in agenda.buscar("lau"):
        print(c)