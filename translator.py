from googletrans import Translator

def translate_text(text, src_language, dest_language):
    translator = Translator()
    translation = translator.translate(text, src=src_language, dest=dest_language)
    return translation.text

def translation_menu():
    print("Welcome to the Translation Menu!")
    print("You can translate between any supported languages.")
    print("Please enter language codes in the ISO 639-1 format (e.g., 'en' for English, 'es' for Spanish).")
    
    # Taking user input for source and destination languages
    src_lang = input("Enter source language code: ").strip()
    dest_lang = input("Enter target language code: ").strip()
    
    # Taking user input for the text to be translated
    text = input("Enter text to translate: ").strip()
    print('Input text ',text)

    if src_lang and dest_lang and text:
        try:
            # Translating the text
            result = translate_text(text, src_lang, dest_lang)
            print(f"Translated text: {result}")
        except Exception as e:
            print(f"Error occurred during translation: {str(e)}")
    else:
        print("Invalid input. Please enter valid language codes and text.")

if __name__ == "__main__":
    translation_menu()
