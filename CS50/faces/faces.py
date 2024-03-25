def convert(text):
    text_replaced = text.replace(":)", "🙂").replace(":(", "🙁")
    return text_replaced

def main():
    text_user = input("Add your text here:")
    print(convert(text_user))

main()
