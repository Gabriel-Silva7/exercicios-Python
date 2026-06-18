from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys

class janela2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha janela")
        # Largura, altura e posição da janela 
        self.setGeometry(10,20,800,400)
        self.texto = QLabel("Clique no botão abaixo")
        self.botao = QPushButton("Clique aqui")
        #
        #
        Layout_vertical = QVBoxLayout()
        Layout_vertical.addWidget(self.texto)
        Layout_vertical.addWidget(self.botao)
        #
        self.setLayout(Layout_vertical)
        
app = QApplication(sys.argv)
tela = janela2()
tela.show()
app.exec()       