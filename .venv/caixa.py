from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTableWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap
from sys import argv 
# importando uma biblioteca de foto com o "from PyQt6.QtGui import QPixmap (Linha 2)

class Caixa(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caixa da Padaria")
        self.setGeometry(150,50,1600,900) # posição x ou y ela abre mais para esquerda e para direita, y mais para cima ou para baixo?

        # criar o layout horizontal
        self.layout_horizontal = QHBoxLayout()
        # vamos criar as duas colunas: esquerda e direita 
        self.label_col_esquerda = QLabel()
        # alterar a cor do fundo da label esquerda 
        self.label_col_esquerda.setStyleSheet("QLabel{background-color:#660000}")
        self.label_col_esquerda.setFixedWidth(800)
        
        # criar o layout dos elementos da coluna da esquerda. Este layout é vertical 
        self.layout_vert_col_esq = QVBoxLayout()

        # vamos criar uma label para adicionar o logo da padaria 
        self.label_logo = QLabel()
        # vamos setar o Pixmap a label para carregar a imagem 
        self.label_logo.setPixmap(QPixmap("IMG/logo.png"))
        # ajustar a imagem a label
        self.label_logo.setScaledContents(True)

        # criar a label do código do produto
        self.label_cod_produto = QLabel("Código do Produto")
        self.label_cod_produto.setStyleSheet("QLabel{font-weight:bold,font-size:15pt;color:#ffffff}")
        self.edit_cod_produto = QLineEdit()
        self.edit_cod_produto.setStyleSheet("QLineEdit{font-size:15pt}")
        self.edit_cod_produto.setFixedHeight(50)






        # criar a label e o edit do nome do prduto -----------------------------------------------------------
        self.label_nome_produto = QLabel("Nome do Produto")
        self.label_nome_produto.setStyleSheet("QLabel{font-weight:bold,font-size:15pt;color:#ffffff}")
        self.edit_nome_produto = QLineEdit()
        self.edit_nome_produto.setStyleSheet("QLineEdit{font-size:15pt}")
        self.edit_nome_produto.setFixedHeight(50)



        # criar a label e o edit da descricao do prduto -----------------------------------------------------------
        self.label_descricao_produto = QLabel("Descrição do Produto")
        self.label_descricao_produto.setStyleSheet("QLabel{font-weight:bold,font-size:15pt;color:#ffffff}")
        self.edit_descricao_produto = QLineEdit()
        self.edit_descricao_produto.setStyleSheet("QLineEdit{font-size:15pt}")
        self.edit_descricao_produto.setFixedHeight(50)




        # criar a label e o edit da quantidade do prduto -----------------------------------------------------------
        self.label_quantidade_produto = QLabel("Quantidade do Produto")
        self.label_quantidade_produto.setStyleSheet("QLabel{font-weight:bold,font-size:15pt;color:#ffffff}")
        self.edit_quantidade_produto = QLineEdit()
        self.edit_quantidade_produto.setStyleSheet("QLineEdit{font-size:15pt}")
        self.edit_quantidade_produto.setFixedHeight(50)




        # criar a label e o edit do preço unitario do prduto -----------------------------------------------------------
        self.label_preco_produto = QLabel("Preço Unitario do Produto")
        self.label_preco_produto.setStyleSheet("QLabel{font-weight:bold,font-size:15pt;color:#ffffff}")
        self.edit_preco_produto = QLineEdit()
        self.edit_preco_produto.setStyleSheet("QLineEdit{font-size:15pt}")
        self.edit_preco_produto.setFixedHeight(50)





        # vamos adicionar a logo ao layout vertical 
        self.layout_vert_col_esq.addWidget(self.label_logo)
        # adicionar o código do produto
        self.layout_vert_col_esq.addWidget(self.label_cod_produto)
        self.layout_vert_col_esq.addWidget(self.edit_cod_produto)


        # adicionar o nome do produto
        self.layout_vert_col_esq.addWidget(self.label_nome_produto)
        self.layout_vert_col_esq.addWidget(self.edit_nome_produto)



        # adicionar a descrição do produto
        self.layout_vert_col_esq.addWidget(self.label_descricao_produto)
        self.layout_vert_col_esq.addWidget(self.edit_descricao_produto)


        # adicionar a quantidade do produto
        self.layout_vert_col_esq.addWidget(self.label_quantidade_produto)
        self.layout_vert_col_esq.addWidget(self.edit_quantidade_produto)

        # adicionar o preço unitario do produto
        self.layout_vert_col_esq.addWidget(self.label_preco_produto)
        self.layout_vert_col_esq.addWidget(self.edit_preco_produto)
      
     



        # setar o layout vertical a label coluna esquerda 
        self.label_col_esquerda.setLayout(self.layout_vert_col_esq)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        self.label_col_direita = QLabel()
        self.label_col_direita.setStyleSheet("QLabel{background-color:#ffff66}")

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # Adicionar as colunas esquerda e direita ao layout horizontal
        self.layout_horizontal.addWidget(self.label_col_esquerda)
        self.layout_horizontal.addWidget(self.label_col_direita)

        # Setar o layout horizontal a nossa janela 
        self.setLayout(self.layout_horizontal)
              

app = QApplication(argv)
janela = Caixa()   
janela.show() 
app.exec()     

