import os
from flask import Flask, render_template, request, send_file
import fitz  # PyMuPDF
from googletrans import Translator
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from werkzeug.utils import secure_filename

# Ajuste o template_folder e static_folder
app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(__file__), 'front-end'),
            static_folder=os.path.join(os.path.dirname(__file__), 'front-end', 'static'))  # Configuração do static_folder

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

translator = Translator()

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])
    return text

def translate_text(text, dest_lang="pt"):
    return translator.translate(text, dest=dest_lang).text

def create_pdf(text, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    y_position = 750

    for line in text.split("\n"):
        if y_position < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y_position = 750

        c.drawString(50, y_position, line)
        y_position -= 20

    c.save()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return "Nenhum arquivo enviado", 400
        
        file = request.files["file"]
        if file.filename == "":
            return "Nenhum arquivo selecionado", 400
        
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        text = extract_text_from_pdf(file_path)
        translated_text = translate_text(text, "pt")

        output_pdf = os.path.join(app.config["OUTPUT_FOLDER"], f"traduzido_{filename}")
        create_pdf(translated_text, output_pdf)

        return send_file(output_pdf, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

