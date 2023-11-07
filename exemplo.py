import nltk
from nltk.chat.util import Chat, reflections

# Defina os pares de padrões e respostas para o chatbot.
pares = [
    [
        r"oi|olá|oi bot",
        ["Oi! Como posso ajudar?", "Olá! Qual é a sua pergunta?", "Olá, como você está?"]
    ],
    [
        r"como você está",
        ["Estou muito bem, em que posso ajudar?"]
    ],
    [
        r"qual é o seu nome?",
        ["Oi eu sou o Ed, um assistente virtual criado pelo CopasturLabs."]
    ],
    [
        r"(adeus|até logo)",
        ["Até logo! Tenha um bom dia.", "Até mais tarde!"]
    ],
    [
        r"obrigado|obrigado bot",
        ["De nada! Estou aqui para ajudar.", "Você é bem-vindo!"]
    ],

     [
        r"o que é o Copastur Labs?",
        ["O o CopasturLabs é o Hub de inovação da Copastur, nosso objetivo é acelerar o processo.", "Você é bem-vindo!"]
    ],
    [
        r"(.*) (ajuda|ajudar)",
        ["Claro, posso ajudá-lo com perguntas simples. O que você gostaria de saber?"]
    ],
]

# Crie um objeto de chatbot e inicie a conversa.
chatbot = Chat(pares, reflections)
print("Olá! Eu sou um chatbot. Digite 'sair' para encerrar o chat.")
while True:
    user_input = input("Você: ")
    if user_input.lower() == 'sair':
        print("Chatbot: Adeus! Espero ter ajudado.")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
