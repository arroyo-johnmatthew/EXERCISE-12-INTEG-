from googletrans import Translator
translator = Translator()
user_input = input("Enter text: ")
user_language = input("Enter language: ")
input_translate = input("Translate to: ")

converted =  translator.translate(user_input, dest = input_translate)
print(f"Translated text: {converted.text}")