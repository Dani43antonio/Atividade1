#jokenpô
resposta ="sim"
jogador1=input("usuario1 digite um nome:")
jogador2=input("usuario2 digite um nome:")
opcao1=input("jogador_1:{pedra, papel, tesoura}")
opcao2=input("jogador_2:{pedra, papel, tesoura}")
if opcao1==opcao2:
    print("empate")
elif opcao1=="pedra" and opcao2=="tesoura":
    print(f"{jogador1} ganhou")
elif opcao1=="tesoura" and opcao2=="papel":
    print(f"{jogador1} ganhou")
elif opcao1=="papel" and opcao2=="pedra":
    print(f"{jogador1} ganhou")
else:
    print("jogador 2 ganhou")