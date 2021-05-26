%{
/*
 exemplos: a=x*z+(w-1)/7
           x2 = 6+y2-(3/5)*f
*/

#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>

int endr(char *);
%}

%union { char *vals; int vali; float valf; }

%token <vals>ID
%token <vali>NUMI
%token <valf>NUMF
%token  <valS>Insts Inst
%type  <vals>Atrib Exp Termo Fator
%type  <vali>Var


%%
Insts : Atrib             { printf("%s\n",$1); }
      ;
Atrib : Var '=' Exp       { asprintf(&$$,"%sSTORE %d\n",$3,$1); }
      ;
Var   : ID                { $$=endr($1); }
      ;
Exp   : Termo             { $$=$1; }
      | Exp '+' Termo     { asprintf(&$$,"%s%sADD \n",$1,$3); }
      | Exp '-' Termo     { asprintf(&$$,"%s%sSUB \n",$1,$3); }
      ;
Termo : Fator             { $$=$1; }
      | Termo '*' Fator   { asprintf(&$$,"%s%sMUL \n",$1,$3); }
      | Termo '/' Fator   { asprintf(&$$,"%s%sDIV \n",$1,$3); }
      ;
Fator : NUMI              { asprintf(&$$,"PUSHI %d\n",$1); }
      | NUMF              { asprintf(&$$,"PUSHF %f\n",$1); }
      | ID                { asprintf(&$$,"LOAD  %d\n",endr($1)); }
      | '(' Exp ')'       { $$=$2; }
      ;


Insts : Inst {$$ = $1;}
      | Insts ';' Inst {asprintf(&$$, "%s %s", $1, $3);}

 %%
}
#include "lex.yy.c"

int endr(char *id){ return 0; }

int yyerror(char *s)
{
  fprintf(stderr, "ERRO: %s \n", s);
}

int main()
{
  yyparse();
  return(0);
}
