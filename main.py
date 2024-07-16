import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel
from PyQt5.QtCore import Qt


class TextAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Analyzer")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.analyze_text)
        self.layout.addWidget(self.text_edit)

        self.counters_layout = QHBoxLayout()
        self.layout.addLayout(self.counters_layout)

        self.results_labels = {
            "Paragraphs": QLabel("Paragraphs: 0"),
            "Sentences": QLabel("Sentences: 0"),
            "Words": QLabel("Words: 0"),
            "Characters (with spaces)": QLabel("Characters (with spaces): 0"),
            "Characters (without spaces)": QLabel("Characters (without spaces): 0")
        }

        for label in self.results_labels.values():
            self.counters_layout.addWidget(label)

    def analyze_text(self):
        text = self.text_edit.toPlainText()

        # Count paragraphs
        paragraphs = len([p for p in text.split('\n') if p.strip()])
        self.results_labels["Paragraphs"].setText(f"Paragraphs: {paragraphs}")

        # Count sentences (simple approach: split by '.', '!', '?')
        sentences = len([sentence for sentence in text.replace('!', '.').replace('?', '.').split('.') if sentence.strip()])
        self.results_labels["Sentences"].setText(f"Sentences: {sentences}")

        # Count words (split by whitespace)
        words = len(text.split())
        self.results_labels["Words"].setText(f"Words: {words}")

        # Count characters (with and without spaces)
        characters_with_spaces = len(text)
        self.results_labels["Characters (with spaces)"].setText(f"Characters (with spaces): {characters_with_spaces}")

        characters_without_spaces = len(text.replace(" ", ""))
        self.results_labels["Characters (without spaces)"].setText(f"Characters (without spaces): {characters_without_spaces}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    analyzer = TextAnalyzer()
    analyzer.show()
    sys.exit(app.exec_())
