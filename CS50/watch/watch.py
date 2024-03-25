import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Define o padrão de expressão regular para extrair a URL do YouTube
    pattern = r'src="(https?://(?:www\.)?youtube\.com/embed/[\w-]+)"'

    # Procura pelo padrão na string de entrada
    match = re.search(pattern, s)

    # Se encontrar uma correspondência, extrai a URL
    if match:
        youtube_url = match.group(1)
        # Converte a URL para o formato youtu.be
        youtu_be_url = re.sub(r'^https?://(?:www\.)?youtube\.com/embed/', 'https://youtu.be/', youtube_url)
        return youtu_be_url
    else:
        return None


if __name__ == "__main__":
    main()
