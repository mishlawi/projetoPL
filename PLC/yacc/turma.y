%{
#include <stdio.h>
#include <strings.h>
/* Declaracoes C diversas */
int conta = 0;
int total = 0;
float media = 0;
float soma = 0;
char *nome;
%}

%union {float val; char *texto;}

%token <texto>STR /*"[^"]*\" */

%token <val>INT /*[0-9]+ */

%token ID /*[a-zA-Z][a-zA-Z0-9]* */

%token TURMA SETA

%type <val>Nota
%type <texto>Nome 



%%

Turma : TURMA ID Elems '.' { printf("total de alunos %d\n", conta);}
      ;

Elems : Elems ';' Elem {printf("media do aluno %s: %f\n",nome, media);}
      | Elem           {printf("media do aluno %s: %f\n", nome, media);}
      ;

Elem : Aluno SETA Notas {media=soma/total;}
     ;


Aluno : Nome  {conta++ ; nome=strdup($1);}
      ;

Notas : Notas ',' Nota {total++; soma+=$3;}
      | Nota           {total=1; soma=$1;}


Nota : INT             {$$= $1;}
     ;

Nome : STR
     ; 


%%

#include "lex.yy.c"

int yyerror(char *s)
{
  fprintf(stderr, "ERRO: %s \n", s);

}

int main()
{
  yyparse();
  return(0);
}