from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
import sys

class cadastroProduto(QWidget):
    # Método init para inicializar a nossa janela 
    def __init__(self):
        super().__init__()
        #vamos setar um texto para o titulo da janela 
        self.setWindowTitle("Cadastro de Produtos")
        # setar a posição e o tamanho da janela 
        self.setGeometry(350,300,300,450)
        self.setStyleSheet("background-color: black;")

        self.nome_label = QLabel("Nome do produto")
        # Vamos aplicar uma formatação na label usando 
        # comandos de CSS(cascade sytle sheet - Folha de Estilo em cascata)
        self.nome_label.setStyleSheet("QLabel{font-size:32px;color:#5e35b1;font-weight:bold}")
        self.nome_edit = QLineEdit()
        self.nome_edit.setStyleSheet("QLineEdit{border-radius:10px; background-color: #DDDDDD; font-size:20pt}")

        self.tipo_label = QLabel("Tipo")
        self.tipo_label.setStyleSheet("QLabel{font-size:32px;color:#5e35b1;font-weight:bold}")
        self.tipo_edit = QLineEdit()
        self.tipo_edit.setStyleSheet("QLineEdit{border-radius:10px; background-color: #DDDDDD; font-size:20pt}")

        self.preco_label = QLabel("Preço")
        self.preco_label.setStyleSheet("QLabel{font-size:32px;color:#5e35b1;font-weight:bold}")
        self.preco_edit = QLineEdit()
        self.preco_edit.setStyleSheet("QLineEdit{border-radius:10px; background-color: #DDDDDD; font-size:20pt}")


        self.cadastrar_button = QPushButton("Cadastrar")
        self.cadastrar_button.setStyleSheet("QPushButton{font-size: 32px; background-color: #5e35b1; font-weight: bold }")

        self.layout_vertical = QVBoxLayout()
        # adicionar os controles ao layout
        self.layout_vertical.addWidget(self.nome_label)
        self.layout_vertical.addWidget(self.nome_edit)

        self.layout_vertical.addWidget(self.tipo_label)
        self.layout_vertical.addWidget(self.tipo_edit)

        self.layout_vertical.addWidget(self.preco_label)
        self.layout_vertical.addWidget(self.preco_edit)

        self.layout_vertical.addWidget(self.cadastrar_button)

        # adicionar o layout vertical com todos os controles a nossa janela 
        self.setLayout(self.layout_vertical)
        




# Apresentar a janela 
app = QApplication(sys.argv)
cad = cadastroProduto()
cad.show()
app.exec()