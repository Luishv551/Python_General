from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 20)  # Increase header font size
        self.cell(0, 10, 'CS50 Shirtificate', 0, 1, 'C')

def generate_shirtificate(name):
    pdf = Shirtificate()
    pdf.add_page()

    # Set font for the name
    pdf.set_font('Arial', '', 16)

    # Add the shirt image
    pdf.image('shirtificate.png', x=50, y=40, w=110)

    # Add the name and prompt
    text = f"{name} took CS50"
    name_width = pdf.get_string_width(text)
    name_x = (210 - name_width) / 2  # Center horizontally
    name_y = 80  # Adjusted position

    # Add the name
    pdf.set_text_color(255, 255, 255)  # White color
    pdf.text(name_x, name_y, text)

    # Output the PDF
    pdf.output('shirtificate.pdf')

def main():
    name = input("Enter your name: ")
    generate_shirtificate(name)

if __name__ == "__main__":
    main()
