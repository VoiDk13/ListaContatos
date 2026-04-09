
import sqlite3
import os
import time

#CRIA ARQUIVO CASO NÂO EXISTIR E SE CONECTA AO BANCO DE DADOS

Conectar = sqlite3.connect("MeusContatos.db")

cursor = Conectar.cursor()

#CRIA TABELA NO BANCO DE DADOS CASO NÂO EXISTIR
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS Contatos(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NOME TEXT,
TELEFONE INTEGER
)
""")

#CRIA FUNÇAO DE CADASTRO DE CLIENTES
def CadastroCliente():
#Cria funçao de cadastrar cliente no banco de dados na tabela Clientes
	def cadastro():
		cursor.execute("""
		INSERT INTO Contatos(
		NOME,
		TELEFONE
		)
		VALUES(?, ?)""",(Nome,Telefone)
		)
		Conectar.commit()
	
	#Define nome do contato e tamanho
	while True:
			
		os.system("clear")
		
		Nome = input("NOME DO CONTATO\n")
		os.system('clear')
		
		if len(Nome) <= 49:
			break
		else:
			print("NOME INVALIDO!!")
			time.sleep(1)
			os.system("clear")
		
	#define Telefône e se é um numero ou não e tamanho	
	while True:
		
		Telefone = input("TELEFONE DO CONTATO\n")
		os.system('clear')
		if Telefone.isdigit() and len(Telefone) <= 18:
			break
		else:
			print("NÚMERO INVÁLIDO!!")
			time.sleep(1)
			os.system('clear')
	
	#Escolha de Salvamento
	while True:
		
		 escolha = input("Deseja Salvar este Cliente(Y/N)\n").upper()
		
		 if escolha == "Y":
			 
			 cadastro()
			 
			 os.system('clear')
			 print("Cliente Salvo com sucesso!!")
			 time.sleep(1)
			 os.system('clear')	
			 break
			 	 
		 if escolha == "N":
			 
			 os.system('clear')
			 break
		 else:
			
			 os.system('clear') 	 
			 
def MostrarTabela():
	
	while True:
		os.system("clear")
		cursor.execute("SELECT * FROM Contatos ORDER BY NOME")
				 
		dados = cursor.fetchall() 
		print("$"*80)
		print("$| ID |"+" NOME "+" "*43+"|| TELEFONE"+" "*11+"|$")
		print("$|"+"──"*38+"|$")
		for ID, Nome, Telefone in dados:
			
			print(f"$|{ID:^4}|{Nome:<49}|| {Telefone:<19}|$")
			
		print("$|"+"_"*76+"|$")	
		print("$"*80)	
		dados = ""
		print("─"*80)
		print("(D)Deletar (A)Adicionar (X)Sair ")
		print("─"*80)
		
		esc = input("INPUT:").upper()
		
		
		if esc == "A":
			
			CadastroCliente()
		if esc == "D":
			DeletaUsuario()
		if esc == "X":
		
			os.system("clear")
			break
	

def DeletaUsuario():
	while True:
		os.system("clear")
		
		cursor.execute("SELECT * FROM Contatos ORDER BY NOME")
				 
		dados = cursor.fetchall() 
		print("$"*80)
		print("$| ID |"+" NOME "+" "*43+"|| TELEFONE"+" "*11+"|$")
		print("$|"+"──"*38+"|$")
		for ID, Nome, Telefone in dados:
			
			print(f"$|{ID:^4}|{Nome:<49}|| {Telefone:<19}|$")
			
		print("$|"+"_"*76+"|$")	
		print("$"*80)	
		dados = ""
		print("─"*80)
		print("*QUAL USUARIO(ID) DELETAR??? | (B)VOLTAR ")
		print("─"*80)
		
		esc = input("INPUT:").upper()
		
		if len(esc) >=1 and esc.isdigit():
			cursor.execute("SELECT * FROM Contatos WHERE ID = ?",(esc))
			
		foundit = cursor.fetchone()
		
		if foundit:
			cursor.execute("DELETE FROM Contatos WHERE ID =(?)",(esc))
			Conectar.commit()
		if esc == "B":
			os.system("clear")
			break
		else:
			os.system("clear")
			


#--------------------------------------------------------------------------------------------------

os.system("clear")

MostrarTabela()
	
	
