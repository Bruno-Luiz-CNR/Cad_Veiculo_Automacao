![1615525831710](https://github.com/Bruno-Luiz-CNR/Cad_Veiculo_Automacao/assets/115126390/8a305ec1-e6ce-4370-baba-64a4dd606aea)



# Cad_Veiculo_Automacao

#Resumo do código:#

Importações:

Utiliza módulos do PySide6 para GUI.
Usa threading para executar tarefas em segundo plano.
Importa módulos relacionados a QMessageBox e expressões regulares.
Classe MainWindow:

Subclasse de QMainWindow e Ui_MainWindow.
Configura a interface gráfica, conecta eventos a métodos.
Possui métodos para atualizar a ListView e executar a pesquisa e automação web.
Usa threading para executar a automação em segundo plano.
Exibe mensagens de erro com o QMessageBox.
executarPesq:

Obtém dados da interface.
Valida entrada.
Inicia a automação em uma thread se as condições são atendidas.
executarAutomacaoWeb:

Chama a função pesquisar() para obter dados da web.
Executa o cadastro se a placa for encontrada.
Lida com exceções e exibe mensagens.
main_areas.py (pesquisar):

Utiliza Selenium para automatizar interações com uma página web.
Realiza login, navega por menus e preenche formulários.
Retorna dados do veículo se encontrado, senão retorna None.
placasiger.py (inseDados):

Utiliza Selenium para automatizar interações em outra página web.
Realiza login, preenche informações do veículo e equipamento.
Trata exceções, retorna True se o cadastro é bem-sucedido.
automacao_thread:

Função que inicia a automação em uma thread separada.
Observações Gerais:

Ambos os módulos de automação utilizam Selenium para interação com páginas web.


