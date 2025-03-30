#05
import emoji

def mostra_emojis():
    emojis = {
        ":red_heart:": "❤️",
        ":thumbs_up:": "👍",
        ":thinking_face:": "🤔",
        ":partying_face:": "🥳",
        ":smiling_face:": "😊",
        ":crying_face:": "😢",
        ":fire:": "🔥",
        ":rocket:": "🚀",
        ":books:": "📚",
        ":computer:": "💻"
    }
    for cod, emoji in emojis.items():
        print(f'{emoji} - {cod}')
        
def emojizar_frase():
    frase = input('Digite uma frase para ser emojizada: ("Ex Ola mundo! :red_heart:) ')
    frase_c_emoji = emoji.emojize(frase, language='alias') # Corresponde ao padão de códigos :red_heart: = padrão de código "alias"
    return frase_c_emoji

def main():
    print('-- Conversor de frase em emojis ---')
    mostra_emojis()
    frase_final = emojizar_frase()
    print(f'Frase com emoji \n {frase_final}')
    
if __name__ == "__main__":
    main()