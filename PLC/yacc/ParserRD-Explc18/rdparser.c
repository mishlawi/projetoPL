#include <stdio.h>
#include <stdlib.h>
#include "lex.yy.c"

#define ERRMSG "Erro ao tentar derivar " 

/*
 * Gramatica a ser reconhecida
 *
 * regPar -> reg regPar
 *        |  $
 * reg    -> '#' data bat
 * reg2   -> bat
 *        |  nasc
 * bat    -> 'batismoDe' nome 
 * nasc   -> 'nascimentoDe' nome 'MAE' nome 'PAI' nome
 * nome   -> String
 *
 */


Token i;

// variaveis que registam o numero de Batismos e Nascimentos respectivamente
int cntBat, cntNasc;

char *nomes[] = { "FDF", "CARDINAL", "DATA", "BATISMO", "NASCIMENTO", "MAE", "PAI", "PALAVRAS" };

char buffer[101];


void erros(char *mensagem) {

	printf("%s -- ", mensagem);
	printf("%s\n", buffer);
	exit(-1);
}

void proxsimb() {

	i = yylex();

}

int aceita(Token f) {

	if (i == f) {
		proxsimb();
		return 1;
	}

	sprintf(buffer, "Erro ao tentar aceitar o token %s", nomes[f]);
	return 0;

}

void nome(void) {
	
	if( !aceita(PALAVRAS) ) {
		erros(ERRMSG "nome.");
	}
}

void nasc(void) {

	int k;

	if( k = aceita(NASCIMENTO) ) {
		nome();
		if( k = aceita(MAE) ) {
			nome();
			if( k = aceita(PAI) ) {
				nome();
				cntNasc++;   // acao semantica associada a reconhecer nasc
			}
		}
	}

	if( !k ) {
		erros(ERRMSG "nasc.");
	} 

}

void bat(void) {

	if( aceita(BATISMO) ) {
		nome();
		cntBat++;  // acao semantica associada a reconhecer bat
	}
	else {
		erros(ERRMSG "bat.");
	}

}

void reg2(void) {

	if(i == BATISMO) {
		bat();
	}
	else if(i == NASCIMENTO) {
		nasc();
	}
	else {
		erros(ERRMSG "reg2.");
	} 
}

void reg(void) {

	int k;

	if( k = aceita(CARDINAL) ) {
	 	if( k = aceita(DATA) ) {
			reg2();
		}		
	}

	if( !k ) {
		erros(ERRMSG "reg."); 
	}
}

void regPar(void) {
	
	if( i == CARDINAL ) {
		reg();
		regPar();
	}
	else if( i == FDF ) {
		;
	}
	else {
		erros(ERRMSG "regPar.");
	}
}

int main(void) {
	
	proxsimb();
	regPar();
	printf("Nr de batismos: %d\nNr de nascimentos: %d\n", cntBat, cntNasc);
	printf("Saida com sucesso!\n");
	return 0;
}
