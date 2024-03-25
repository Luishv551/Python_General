import sys
import csv

def clean_names(input_file, output_file):
    try:
        with open(input_file, newline='') as f:
            reader = csv.reader(f)
            with open(output_file, 'w', newline='') as f_out:
                writer = csv.writer(f_out)
                writer.writerow(["first", "last", "house"])  # Escreve o cabeçalho no arquivo de saída
                next(reader)  # Ignora a primeira linha (cabeçalho) do arquivo de entrada
                for row in reader:
                    full_name = row[0].strip('"')
                    if ',' in full_name:  # Verifica se o nome já está no formato "sobrenome, nome"
                        last_name, first_name = full_name.split(', ')
                    else:  # Se não estiver, assume que o último elemento é o sobrenome
                        last_name = full_name.split()[-1]
                        first_name = ' '.join(full_name.split()[:-1])
                    writer.writerow([first_name, last_name, row[1]])
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Too few or too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    clean_names(input_file, output_file)
