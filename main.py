import threading
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui_main import Ui_MainWindow
from main_areas import pesquisar
from placasiger import inseDados
from PySide6.QtWidgets import QMessageBox
import sys
import re


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadastro Veiculo Cllick")
        appIcon = QIcon(u"imb/iconcllick.ico")
        self.setWindowIcon(appIcon)
        self.btn_cadastrar.clicked.connect(self.executarPesq)

    def updateListView(self, text):
        self.List_View.addItem(text)

    def executarPesq(self):
        placa = self.txt_placa.text().upper()
        equip = self.txt_equipamento.text()
        if re.match("^[0-9]+$", equip):
            equipamentos = len(equip)
            character_count = len(placa)
            if character_count > 6 and equipamentos >= 4:
                self.List_View.addItem(f"Coletando informações do sistema SAT")
                self.progressBar.setValue(20)
                automation_thread = threading.Thread(target=self.executarAutomacaoWeb, args=(placa, equip))
                automation_thread.start()
            else:
                QMessageBox.about(self, "Preencha corretamente os campos", "Verificar informações digitadas!!")
                self.List_View.addItem(f"Favor Verificar Placa digitada: {placa} ou Equipamento: {equip}!!")
        else:
            QMessageBox.about(self, "Equipamento", " Favor digitar numero de equipamento válido!")

    def executarAutomacaoWeb(self, placa, equip):
        try:
            resultado_pesquisa = pesquisar(placa)
            if resultado_pesquisa[7]:  # Verifique se a placa foi encontrada (True)
                placa, modelo, ano, cor, chassi, ren, cliente, _ = resultado_pesquisa  # Ignorando o último valor
                self.List_View.addItem(f"Todos os dados da placa: {placa} foram coletados com sucesso!")
                self.List_View.addItem(f"Aguardando SystemSat para cadastro de informações !")
                self.executar_cadastro(placa, modelo, ano, cor, chassi, ren, cliente, equip)
            else:
                self.List_View.addItem(f"Placa não encontrada: {placa}")

        except Exception as e:
            self.updateListView(f"Erro ao inserir informações na SSX: {e}")

    def executar_cadastro(self, placa, modelo, ano, cor, chassi, ren, cliente, equip):
        try:
            inseDados(placa, modelo, ano, cor, chassi, ren, cliente, equip)
            self.updateListView(f"Placa cadastrada com Sucesso!!!")
            self.progressBar.setValue(100)

        except Exception as e:
            self.updateListView(f"Tempo excedido para efetuar cadastro", e)
            self.progressBar.setValue(100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
