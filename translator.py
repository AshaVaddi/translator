from googletrans import Translator

def translate_text(text, src_language, dest_language):
    translator = Translator()
    translation = translator.translate(text, src=src_language, dest=dest_language)
    return translation.text

def translation_menu():
    while True: 
        print("Welcome to the Translation Menu!")
        print("You can translate between any supported languages.")
        print("Please enter language codes in the ISO 639-1 format (e.g., 'en' for English, 'es' for Spanish).")
        
        src_lang = input("Enter source language code: ").strip()
        dest_lang = input("Enter target language code: ").strip()
        
        text = input("Enter text to translate: ").strip()
        
        print('Entered source language:', src_lang)
        print('Entered target language:', dest_lang)
        print('Input text:', text)

        if src_lang and dest_lang and text:
            try:
                result = translate_text(text, src_lang, dest_lang)
                print(f"Translated text: {result}")
            except Exception as e:
                print(f"Error occurred during translation: {str(e)}")
        else:
            print("Invalid input. Please enter valid language codes and text.")

        choice = input("Do you want to translate another text? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exiting the program. Goodbye!")
            break 

if __name__ == "__main__":
    translation_menu()
