
%union {char *vals; int vali; float valf;}
%token <vals>ID
%token <vali>NUMI
%token <valf>NUMF

%type <vals>Var

%% 

Inst : Atrib
     ;

Atrib : Var '=' Exp  {printf("STORE %d\n",end($1));}
      ;

Var : ID             {$$=strdup($1);}
    | ID '[' Exp ']'
    ;

Exp : Termo
    | Exp '+' Termo  {printf("ADD\n");}
    | Exp '-' Termo  {printf("SUB\n");}
    ;

Termo : Fator
      | Termo '*' Fator {printf("MUL\n");}
      | Termo '\' Fator {printf("DIV\n");}
      ;

Fator : NUMI  {printf("PUSHI %d\n", $1);}
      | NUMF  {printf("PUSHF" %f\n, $1);}
      | ID    {printf("LOAD %d\n", end($1));}
      | '(' Exp ')'
      ;

ExpH : Exp 
     | Exp OPREL Exp
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