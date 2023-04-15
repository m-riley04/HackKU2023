from components.window import App
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication([])
    window = App()
    app.exec()

if __name__ == "__main__":
    main()