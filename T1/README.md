# Trabalho IDL - README DESATUALIZADO

*Arquiteturas de Sistemas Distribuídos, Paralelos e Concorrentes*
*Escola Politécnica - PUCPR*
*(C) 2019 by Prof. Luiz A. de P. Lima Jr.*
*luiz.lima@pucpr.br*

## Diretórios:

    * idl: arquivo IDL + stub + skeleton
    * bin: executáveis (os resultados das compilações são gerados aqui)
    * client: cliente básico
    * server: servidor básico

## Para gerar stub e skeleton, digite:

	$ cd idl
	$ tao_idl -Gstl Conta.idl

## Para compilar, digite:

	$ cd cliente            # (ou cd servidor)
	$ make
