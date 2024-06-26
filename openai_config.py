import openai

def interactuar_con_openai(mensaje):
    respuesta = openai.Completion.create(
        model="text-davinci-003",
        prompt=mensaje,
        max_tokens=150
    )
    return respuesta.choices[0].text.strip()


