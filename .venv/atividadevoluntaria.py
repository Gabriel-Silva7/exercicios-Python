# 1. IMPORTAÇÕES
# Traz as ferramentas do PyQt6


from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap 
from PyQt6.QtCore import Qt
from sys import argv








#-----------------------------------------------------------------------------------------------------------

# 2. CLASSE DA JANELA
# Cria a janela principal

class CadastroVoluntario(QWidget):

    def __init__(self):

        # Prepara o QWidget
        super().__init__()

        # Título da janela
        self.setWindowTitle("Cadastro de Voluntário")

        # Tamanho da janela
        self.setGeometry(150, 50, 1200, 700)







#-------------------------------------------------------------------------------------------------------------


# 3. CONFIGURAÇÃO DA JANELA
# Título, tamanho, ícone









#-------------------------------------------------------------------------------------------------------------


# 4. CRIAÇÃO DOS LAYOUTS
        # Primeiro criamos a estrutura

        # layout principal da janela
        self.layout_horizontal = QHBoxLayout()

        # coluna esquerda
        self.layout_coluna_esquerda = QVBoxLayout()


        # coluna direita 
        self.layout_coluna_direita = QVBoxLayout()

       # diminui o espaço entre os widgets
        self.layout_coluna_direita.setAlignment(Qt.AlignmentFlag.AlignTop)

        # diminui o espaço entre cada QLabel e QLineEdit
        self.layout_coluna_direita.setSpacing(5)

        


        



        # Colocamos os dois layouts verticais dentro do layout horizontal
        self.layout_horizontal.addLayout(self.layout_coluna_esquerda)
        self.layout_horizontal.addLayout(self.layout_coluna_direita)

        # Colocamos o layout principal dentro da janela
        self.setLayout(self.layout_horizontal)









#-------------------------------------------------------------------------------------------------------------

# 5. COLUNA ESQUERDA
# Criamos os widgets da esquerda
# Imagem do cachorro

        # criando a QLabel vazia para receber a imagem do cachorro
        self.label_dog = QLabel()   


        # vamos colocar a imagem dentro da QLabel   
        self.label_dog.setPixmap(QPixmap("dog.png"))

        self.label_dog.setScaledContents(True)

        self.label_dog.setFixedSize(550, 650)


        self.layout_coluna_esquerda.addWidget(self.label_dog) 

       
        # layout das redes sociais 

        self.layout_redes_direita = QHBoxLayout()

        # centraliza os ícones
        self.layout_redes_direita.setAlignment(Qt.AlignmentFlag.AlignCenter)


        # espaço entre facebook e instagram
        self.layout_redes_direita.setSpacing(30)
       
       
       
        # logo face
        self.label_face = QLabel()
        self.label_face.setPixmap(QPixmap("face.png").scaled(48, 48))
        self.layout_redes_direita.addWidget(self.label_face)

        #logo insta
        self.label_insta = QLabel()
        self.label_insta.setPixmap(QPixmap("insta.jpg").scaled(48, 48))  
        self.layout_redes_direita.addWidget(self.label_insta)












#-------------------------------------------------------------------------------------------------------------

# 6. COLUNA DIREITA
# Criamos os widgets da direita
# Depois adicionamos no layout da direita


 

 
 
 
# TITULO 
        self.label_titulo = QLabel("Seja Voluntário")

        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter) # centralizando o titulo

        self.label_titulo.setStyleSheet(""" font-size: 32pt; font-weight: bold; color: #ff8c42 """)

        
        self.label_subtitulo = QLabel("E ajude um aumigo a encontrar um lar")

        self.label_subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter) # centralizando o subtitulo

        self.label_subtitulo.setStyleSheet(""" font-size: 12pt; color: #555555; """) 
 
 #------------------------------------------------------------------------------------------
  
        self.layout_coluna_direita.addSpacing(50)
  
  # titulo e subtitulo
        self.layout_coluna_direita.addWidget(self.label_titulo)
        self.layout_coluna_direita.addWidget(self.label_subtitulo)



 # nome do voluntario
        self.label_nome = QLabel("Digite seu nome")
        self.edit_nome = QLineEdit()

        # email
        self.label_email = QLabel("Digite seu Email")
        self.edit_email = QLineEdit()

        # senha
        self.label_senha = QLabel("Digite uma senha")
        self.edit_senha = QLineEdit()
        self.edit_senha.setEchoMode(QLineEdit.EchoMode.Password) # escondendo a senha hehesss


        # botão de cadastrar 
        self.botao_cadastrar = QPushButton("Cadastrar")
        
        # estilo do botão
        self.botao_cadastrar.setStyleSheet(""" QPushButton{background-color: #ff8c42; color: white; font-size: 14pt; font-weight: bold} QPushButton:hover{background-color: #e86f20;}""")
        
        self.layout_coluna_direita.addWidget(self.label_nome)
        self.layout_coluna_direita.addWidget(self.edit_nome)
        self.edit_nome.setStyleSheet(""" QLineEdit{border:2px solid #ff8c42; border-radius: 5px; font-size 12pt; padding: 5px;} """)                          

        self.layout_coluna_direita.addWidget(self.label_email)
        self.layout_coluna_direita.addWidget(self.edit_email)
        self.edit_email.setStyleSheet(""" QLineEdit{border:2px solid #ff8c42; border-radius: 5px; font-size 12pt; padding: 5px;} """)

        self.layout_coluna_direita.addWidget(self.label_senha)
        self.layout_coluna_direita.addWidget(self.edit_senha)
        self.edit_senha.setStyleSheet(""" QLineEdit{border:2px solid #ff8c42; border-radius: 5px; font-size 12pt; padding: 5px;}  """)

        self.layout_coluna_direita.addWidget(self.botao_cadastrar)

        self.layout_coluna_direita.addLayout(self.layout_redes_direita)












#-------------------------------------------------------------------------------------------------------------

# 7. ADICIONAR AS COLUNAS NO LAYOUT PRINCIPAL
# Só fazemos isso depois que as colunas já estão prontas










#-------------------------------------------------------------------------------------------------------------

# 8. SETAR O LAYOUT NA JANELA
# Coloca tudo dentro da janela








#-------------------------------------------------------------------------------------------------------------






app = QApplication(argv)

janela = CadastroVoluntario()

janela.show()

app.exec()