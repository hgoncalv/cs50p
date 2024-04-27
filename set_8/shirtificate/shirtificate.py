from fpdf import FPDF

class Shirt:
    def __init__(self, name):
        self.name = name
        self.write_shirt()

    @classmethod
    def get(self):
        name = input("Full name: ").strip()
        return self(name)

    def write_shirt(self):
        pdf = FPDF(orientation="portrait", format="A4")
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)

        pdf.set_font("helvetica", "B", size=46)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 50, border=0, align="C", text="CS50 Shirtificate")
        pdf.ln()

        page_width = pdf.w
        image_width = 180
        x_coordinate = (page_width - image_width) / 2

        pdf.image(
            "shirtificate.png",
            x=x_coordinate,
            y=(297 / 4),
            w=image_width,
            alt_text=f"A Harvard shirt with the words: {self.name} took CS50",
        )

        pdf.set_font("helvetica", "B", size=28)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 150, border=0, align="C", text=f"{self.name} took CS50")
        pdf.output("shirtificate.pdf")


def main():
    Shirt.get()


if __name__ == "__main__":
    main()
