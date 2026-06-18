# ================================================================= CRIAÇÃO JANELA ================================================================================================
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTableWidget, QVBoxLayout, QHBoxLayout, QTableWidgetItem
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from sys import argv 

class Caixa(QWidget):
    
    def __init__(self):
        self.linha = 0
        self.valor_total = 0.0


        super().__init__()
        self.setWindowTitle("Caixa da Padaria")
        self.setGeometry(150,50,1600,900)

        self.setWindowIcon(QIcon("pao.png"))


# =============================================================== CRIAÇÃO LAYOUTS ======================================================================================
        # Criar o layout horizontal ---------------------------------------------------------------------------------------
        self.layout_horizontal = QHBoxLayout()


        # Vamos criar as duas colunas: Esquerda e Direita
        # e alterar as cores de fundo de cada uma:

        self.label_col_esquerda = QLabel()
        self.label_col_esquerda.setStyleSheet("QLabel{background-color:#2C3740}")

        self.label_col_direita = QLabel()
        self.label_col_direita.setStyleSheet("QLabel{background-color:#356BDA}")
        self.label_col_esquerda.setFixedWidth(800)


        # ========================================================== COLUNA ESQUERDA ========================================================================================
        # Criar o layout dos elementos da coluna da esquerda. Este layout é vertical --------------------------------------------------------------------------------------
        self.layout_vert_col_esq = QVBoxLayout()


        # vamos criar uma label para adicionar o logo 
        self.label_logo = QLabel()
        # Vamos setar o Pixmap à label para carregar a imagem
        self.label_logo.setPixmap(QPixmap("img/padariaaa.png"))
        # Ajustar a imagem à label
        self.label_logo.setScaledContents(True)

        
        # criar a label do codigo do produto ----------------------------------------------------------------------------------
        self.label_cod_produto = QLabel("Código do Produto")
        self.label_cod_produto.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#ffffff}")
        self.edit_cod_produto = QLineEdit()
        self.edit_cod_produto.setStyleSheet("QLineEdit{font-size:15pt}")


        # criar a label e o edit do nome do produto ----------------------------------------------------------------------------------
        self.label_nome_produto = QLabel("Nome do Produto")
        self.label_nome_produto.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#ffffff}")
        self.edit_nome_produto = QLineEdit()
        self.edit_nome_produto.setStyleSheet("QLineEdit{font-size:15pt}")


        # criar a label e o edit da descrição do produto ----------------------------------------------------------------------------------
        self.label_descricao_produto = QLabel("Descrição do Produto")
        self.label_descricao_produto.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#ffffff}")
        self.edit_descricao_produto = QLineEdit()
        self.edit_descricao_produto.setStyleSheet("QLineEdit{font-size:15pt}")
        self.edit_descricao_produto.setFixedHeight(88)


        # criar a label e o edit da Quantidade do produto ----------------------------------------------------------------------------------
        self.label_quantidade_produto = QLabel("Quantidade do Produto")
        self.label_quantidade_produto.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#ffffff}")
        self.edit_quantidade_produto = QLineEdit()
        self.edit_quantidade_produto.setStyleSheet("QLineEdit{font-size:15pt}")
        self.edit_quantidade_produto.setFixedHeight(40)


        # criar a label e o edit do preço unitario do produto ----------------------------------------------------------------------------------
        self.label_preco_produto = QLabel("Preço Unitário do Produto")
        self.label_preco_produto.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#ffffff}")
        self.edit_preco_produto = QLineEdit()
        self.edit_preco_produto.setStyleSheet("QLineEdit{font-size:15pt}")
        self.edit_preco_produto.setFixedHeight(40)


        # criar a label e o edit do subtotal do produto ----------------------------------------------------------------------------------
        self.label_subtotal_produto = QLabel("SubTotal:")
        self.label_subtotal_produto.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#ffffff}")
        self.edit_subtotal_produto = QLineEdit("tecle f3 para calcular o sub total")
        self.edit_subtotal_produto.setStyleSheet("QLineEdit{font-size:15pt}")
        self.edit_subtotal_produto.setFixedHeight(40)
        self.edit_subtotal_produto.setEnabled(False)     #serve para bloquear a ediçao da linha pelo usuario



        # Adicionando os elementos á coluna da esquerda --------------------------------------------------------------------------------------------------------
        # Adicionar o logo ao layout vertical
        self.layout_vert_col_esq.addWidget(self.label_logo)

        # Adicionar o codigo do produto
        self.layout_vert_col_esq.addWidget(self.label_cod_produto)
        self.layout_vert_col_esq.addWidget(self.edit_cod_produto)

        # Adicionar o nome do produto
        self.layout_vert_col_esq.addWidget(self.label_nome_produto)
        self.layout_vert_col_esq.addWidget(self.edit_nome_produto)

        # Adicionar a descrição do produto
        self.layout_vert_col_esq.addWidget(self.label_descricao_produto)
        self.layout_vert_col_esq.addWidget(self.edit_descricao_produto)

        # Adicionar a quantidade do produto
        self.layout_vert_col_esq.addWidget(self.label_quantidade_produto)
        self.layout_vert_col_esq.addWidget(self.edit_quantidade_produto)

        # Adicionar o preço do produto
        self.layout_vert_col_esq.addWidget(self.label_preco_produto)
        self.layout_vert_col_esq.addWidget(self.edit_preco_produto)

        # Adicionar o subtotal
        self.layout_vert_col_esq.addWidget(self.label_subtotal_produto)
        self.layout_vert_col_esq.addWidget(self.edit_subtotal_produto)



        # Setar o layout vertical à label coluna esquerda
        self.label_col_esquerda.setLayout(self.layout_vert_col_esq)
#======================================================================== FIM COLUNA ESQUERDA ===============================================================================

#====================================================================== INICIO DA LINHA DIREITA==============================================================================






        self.label_col_direita = QLabel()
        self.label_col_direita.setStyleSheet("QLabel{background-color:#2C3740}")

        self.layout_vert_col_dir = QVBoxLayout()

        self.tabel_produtos = QTableWidget()
       #criar os itens do cabecalho
        cabecalho = ["cod.produto", "nome do produto", "quantidade", "preço", "subtotal"]
        # definir a quantidade de colunas da nossa tabela 
        self.tabel_produtos.setColumnCount(5)
        #adicionar o cabeçalho a tabela 
        self.tabel_produtos.setHorizontalHeaderLabels(cabecalho)
        # adicionar algumas linhas 
        self.tabel_produtos.setRowCount(20)



        self.label_total_pagar = QLabel("total a pagar")
        self.label_total_pagar.setStyleSheet("color:#ffffff;font-size:50pt;font-weight:bold")

        self.edit_total_pagar = QLineEdit("0,00")
        self.edit_total_pagar.setStyleSheet("QLineEdit{font-size:60pt;font-weight:bold; color:#ffffff}")
        self.edit_total_pagar.setEnabled( False)



        #adicionar os controles ao layout vercal da col direita
        self.layout_vert_col_dir.addWidget(self.tabel_produtos)
        self.layout_vert_col_dir.addWidget(self.label_total_pagar)
        self.layout_vert_col_dir.addWidget(self.edit_total_pagar)

        #setar o layout vertical sa col direita na col da direita
        self.label_col_direita.setLayout(self.layout_vert_col_dir)


        # ================================================================== ADICIONAR OS LAYOUTS NA JANELA ==============================================================
                # Adicionar as colunas da esquerda e direita ao layout horizontal
                # lembrar que essa parte tem que sempre ficar depois de ter alterado todos
                # os detalhes doque irá ficar dentro
        self.layout_horizontal.addWidget(self.label_col_esquerda)
        self.layout_horizontal.addWidget(self.label_col_direita)

        # Setar o layout horizontal à nossa janela
        self.setLayout(self.layout_horizontal)

        #vamos usar a funçao  keypress para fzaer a janela 
        #observar as teclas que estao sendo digitadas
        #e assim capturar a tecla especifica e executar 
        #uma açao


        self.keyPressEvent = self.keyPressEvent           # um evento sera disparado quando vc acionar uma tecla

    def keyPressEvent(self, e):
        if(e.key() == Qt.Key.Key_F3):
                sub = float(self.edit_quantidade_produto.text()) *float(self.edit_preco_produto.text())
                self.edit_subtotal_produto.setText(str(sub))


                self.tabel_produtos.setItem(self.linha,0,QTableWidgetItem(self.edit_cod_produto.text()))
                self.tabel_produtos.setItem(self.linha,1,QTableWidgetItem(self.edit_nome_produto.text()))
                self.tabel_produtos.setItem(self.linha,2,QTableWidgetItem(self.edit_quantidade_produto.text()))
                self.tabel_produtos.setItem(self.linha,3,QTableWidgetItem(self.edit_preco_produto.text()))
                self.tabel_produtos.setItem(self.linha,4,QTableWidgetItem(self.edit_subtotal_produto.text()))
                self.linha=+1 # a linha começa com zero ela vai adicionar mais um e vai descer uma linha

                self.valor_total+=sub # colocando o + ele vai adicionando mais produtos no valor total, se voce usar somente o = ele vai substituir o valor do produto
                # entao  tem que ser += para ir adicionando mais valores do produtos, ex: ovo + leite = ....

                self.edit_total_pagar.setText(str(self.valor_total))

                self.edit_cod_produto.setText("")
                self.edit_nome_produto.setText("")
                self.edit_quantidade_produto.setText("")
                self.edit_descricao_produto.setText("")
                self.edit_preco_produto.setText("")
                self.edit_subtotal_produto.setText("Tecle F3 para calcular o sub total")     
                

app = QApplication(argv)
janela = Caixa()
janela.show()
app.exec()



































































































































































































































