%{
#include <stdio.h>
#include <strings.h>
/* Declaracoes C diversas */
%}

%union {char *texto;}

%token LISTA
%token Seccoes
%token <texto>IDsec
%token <texto>STRING
%token INT


%%
Compras : LISTA Seccoes '.'
        ;

Seccoes : Seccao
        | Seccoes Seccao 
        ;

Seccao  : IdSec ':' Itens
        ;

IdSec   : STRING
        ;

Itens   : Item
        | Itens ';' Item
        ;

Item    : STRING '.' INT
        ;

%%

int yyerror(char *s)
{
  fprintf(stderr, "ERRO: %s \n", s);
}

int main()
{
  yyparse();
  return(0);
}