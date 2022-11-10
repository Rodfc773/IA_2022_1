########################### Conjunto das regras #############################3
# 1º QUESTÃO:

# MP: P  => Q, P produz Q
# MT: ¬Q => ¬P, ¬Q produz ¬P
#SH: Silogismo Hipotético: P => Q , Q => R produz P => R
#SD: Silogismo Disjuntivo: P v Q , ~P produz Q

#2º QUESTÃO:
#R1: SE K = sim & L = sim & M = sim ENTÃO I = sim
#R2: SE I = sim & L = sim & J = sim ENTÃO Q = sim
#R3: SE C = sim & D = sim & E = sim ENTÃO B = sim
#R4: SE A = sim & B = sim ENTÃO Q = sim
#R5: SE L = sim & N = sim & O = sim & P = sim ENTÃO Q = sim
#R6: SE C = sim & H = sim ENTÃO R = sim
#R7: SE R = sim & J = sim & M = sim ENTÃO S = sim
#R8: SE F = sim & H = sim ENTÃO B = sim
#R9: SE G = sim ENTÃO F = sim

# ############################# DICIONARIO ##############################
#O programa aceita só átomos lógico, por isso no exemplo de  uma operação Báncaria os objeto serão representados
# da seguinte maneira:

# Cartão = C
# Data = D
# Senha = E
# Tentativas = T
# Saldo = S
# Limite = L
# Pagamento = P
# INSIRA AS REGRAS 

import sys

import shell


def main() -> None:
    try:
        if sys.argv[1:]:
            return shell.fparse(sys.argv[1])
        print("####################################################")
        print("############# WELCOME - ENTER THE RULES ############")
        print("Grammar:")
        print("(+ = binary and) (| = binary or) (^ = binary xor) (! = unary not)")
        print("(=> = implication) (<=> = bi-diretinal implication) (=ARGS  = fact list) (?ARGS = hypothesis list)")
        print("")
        print('Type "quit" to exit the program.')
        return shell.stdin_parse()
    except (EOFError, KeyboardInterrupt):
        exit("Goodbye !")
    except Exception as e:
        exit(e)


if __name__ == "__main__":
    main()  