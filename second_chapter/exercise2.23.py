
def emotion_translator(words: str) -> str:
    if type(words) is not str or len(words.strip()) == 0: return "Neutro 😐"
    for word in words.split(" "):
        match word:
            case "feliz": return "Você está feliz 😃"
            case "triste": return "Você está triste 😞"
            case "nervoso": return "Você está com raiva 😡"

    return "Neutro 😐"



print(emotion_translator(input("Enter: ")))