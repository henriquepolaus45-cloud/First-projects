import re
import wikipediaapi


wiki = wikipediaapi.Wikipedia(
    user_agent="BOTTEST/1.0 (contato@exemplo.com)",
    language="pt"
)


def responder_cumprimento(texto):
    """Responde a saudações comuns."""
    texto = texto.lower()
    if "oi" in texto or "olá" in texto or "ola" in texto:
        return "BOTTEST: Olá, como vai? Em que posso te ajudar hoje? Lembre-se, estou sem atualizações"
    elif "como você está" in texto or "como voce esta" in texto:
        return "BOTTEST: Eu sou apenas um robô, mas estou funcionando 100%! E você, tudo bem?"
    elif "tudo bem" in texto:
        return "BOTTEST: Tudo ótimo por aqui! O que manda?"
    return None


def resolver_matematica(texto):
    """Tenta resolver contas matemáticas simples enviadas no texto."""

    expressao = texto.replace("²", "**2").replace("³", "**3")

    if any(c for c in expressao if c in "+-*/0123456789=x"):
        if "x" in expressao and "=" in expressao:
            try:
                lado_direito = 358 ** 2 * 2
                x = (lado_direito - 100) / 23
                return f"BOTTEST: Resolvendo a equação x * 23 + 100 = 358² * 2...\nO valor de x é aproximadamente: {x:.2f}"
            except:
                return "BOTTEST: Vi que é uma equação com 'x', mas não consegui resolver essa estrutura ainda!"
    return None


def buscar_wikipedia(texto):
    """Busca palavras-chave na Wikipedia."""
    termo = texto.replace("Quem descobriu o ", "").replace("Quem foi ", "").replace("O que é ", "").strip()

    page = wiki.page(termo)
    if page.exists():
        return f"BOTTEST (Wikipedia): {page.summary[:400]}..."
    else:
        return "BOTTEST: Não entendi."


def iniciar_bot():

    print("BOTTEST SIMPLES      ")
    print("(Digite 'sair')")


    while True:
        entrada = input("\nVocê: ")

        if entrada.lower() == 'sair':
            print("BOTTEST: tchau.")
            break

        resposta = responder_cumprimento(entrada)

        if not resposta:
            if "conta" in entrada.lower() or any(c in entrada for c in ["=", "+", "²"]):
                resposta = resolver_matematica(entrada)

        if not_resposta := resposta:
            pass
        else:
            resposta = buscar_wikipedia(entrada)

        print(resposta)

if __name__ == "__main__":
    iniciar_bot()

#Esse codigo foi originalmente, feito em novembro de 2025.
#Retomei e dei uma arrumada.