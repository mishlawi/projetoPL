
%{
#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "hashtable.c"
#include "stack.h"



FILE *f;
char erros[1024] = "";
int numeroLinha = 1;
int countVar = 0;
int type = 0;

stack label;
int labelcounterSE=-1;
int labelcounterENQUANTO=-1;


HashTable hashTableVar;


void insereVariavel( HashTable, char *, int);
void erroAtribuicao(int numeroLinha, char *variavel);
void erroDeclaracaow(int numeroLinha, char *variavel);









%}


%union { char *vals; int vali; float valf;  char *valb;}

%token <vals>ID
%token <vali>NUMI
%token <valf>NUMF
%token <valb>NBOOL
%token <vals>STR
%token SE SENAO 
%token ENQUANTO
%token INICIO FIM ENVIA RECEBE 
%token INTEIRO REAL BOOL


%type <vals>Variavel



%start Programa


%%


Programa : Topo Corpo   { fprintf(f,"stop\n"); } 
         ;

Topo   : Declaracao    { fprintf(f,"start\n"); }     
       | Topo Declaracao    
      ;

Declaracao : Tipo Variaveis ';'  
           ;

Tipo : INTEIRO  {type = 0;}
     | REAL     {type = 1;}
     | BOOL     {type = 2;}
     | STR      {type = 3;}
     ;


Variaveis : Variaveis ',' Variavel  { insereVariavel(hashTableVar,$3,type);}
           | Variavel  { insereVariavel(hashTableVar,$1,type);}
           ;

Variavel : ID {$$ = strdup($1);}
         ;

Corpo : INICIO Instrucoes FIM
      ;

Instrucoes : Instrucoes  Instrucao
           | Instrucao
           ;

Instrucao : Condicao 
          | Ciclo 
          | IO ';'
          | Atribuicao ';'
          ;

Atribuicao : Variavel '=' Operacao {fprintf(f,"\tstoreg %d\n",getEndereco(hashTableVar,$1));}
           ;  


Condicao : SE {
              labelcounterSE++;
              fprintf(f,"iflabel%d:\n",labelcounterSE);
              }
              '(' Operacao')' ':' {fprintf(f,"jz elseLabel%d:\n",labelcounterSE);}
              '{' Instrucoes '}'  
              SENAO 
              { 
                fprintf(f,"jump filabel%d\n elseLabel%d\n",labelcounterSE, labelcounterSE);
              } '{' Instrucoes '}' {fprintf(f,"filabel%d:\n",labelcounterSE);}
         | SE {
              labelcounterSE++;
               fprintf(f,"iflabel%d:\n",labelcounterSE);
               }
               '(' Operacao')' ':' '{' Instrucoes '}'
         ;

Ciclo : ENQUANTO 
                {
                labelcounterENQUANTO++;
                fprintf(f,"Whilelabel%d:\n",labelcounterENQUANTO); 
                }'(' Operacao')' ':' {fprintf(f,"jz fiWhileLabel%d:\n",labelcounterENQUANTO);}
                 '{' Instrucoes '}' {fprintf(f,"jump Whilelabel%d\n",labelcounterENQUANTO); 
                                    fprintf(f,"fiWhilelabel%d:\n",labelcounterENQUANTO);}
                
      ;

Operacao : Exp '!' '=' Exp   {fprintf(f,"\tequal\n \tnot \n");}
         | Exp '=' '=' Exp   { fprintf(f,"\tequal\n"); }
         | Exp '<' '='  Exp  { if(type==0){fprintf(f,"\tinfeq\n");}
                               else if(type == 1){fprintf(f,"\tfinfeq\n");} 
                             }
         | Exp '>' '='  Exp  { if(type ==0){fprintf(f,"\tsupeq\n");}
                               else if(type ==1) {fprintf(f,"\tfsupeq\n");}
                             }
         | Exp '<' Exp       { if(type ==0) {fprintf(f,"\tinf\n");}
                               else if(type ==1){fprintf(f,"\tfinf\n");}
                             }
         | Exp '>' Exp       { if(type ==0) {fprintf(f,"\tsup\n");}
                               else if(type ==1) {fprintf(f,"\tsup\n");}
                             }
         | Exp 
         ;

Exp   : Termo             
      | Exp '+' Termo      { if(type == 0) {fprintf(f,"\tadd\n");} 
                             else if(type ==1) {fprintf(f,"\tfadd\n");}
                             }
      | Exp '-' Termo      { if(type == 0) {fprintf(f,"\tsub\n");}
                             else if(type == 1){fprintf(f,"\tfsub\n");}
                            }
      ;

Termo : Fator           
      | Termo '*' Fator   { if(type == 0){fprintf(f,"\tmul\n");}
                            else if(type == 1) {fprintf(f,"\tfmul\n");}
                           }
      | Termo '/' Fator   { if(type == 0){fprintf(f,"\tdiv\n");}
                            else if(type == 1){fprintf(f,"\tfdiv\n");}
                          }
      ;


Fator : NUMI         {  fprintf(f,"\tpushi %d\n",$1); 
                       

                     }                
      | NUMF         {  fprintf(f,"\tpushf %f\n",$1);
                       

                     } 

      | ID           {  {if(getType(hashTableVar,$1) == 0)
                          fprintf(f,"\tpushg %d\n",getEndereco(hashTableVar,$1));

                          }
                         {
                        if(getType(hashTableVar,$1) == 1)
                          fprintf(f,"\tpushg %d\n",getEndereco(hashTableVar,$1));
                          
                          }
                      }
          

      | NBOOL        {  fprintf(f,"\tpushs %s\n",$1); }            
      | '(' Exp ')'  {}

      ;



IO : Output
   | Input
   ;

Output : ENVIA NUMI { fprintf(f,"\twritei\n"); }
       | ENVIA NUMF { fprintf(f,"\twritef\n"); }
       | ENVIA ID   { fprintf(f,"\tpushg %d\n", getEndereco(hashTableVar,$2));
                      if(getType(hashTableVar,$2) == 0)
                        fprintf(f,"\twritei\n");
                      if(getType(hashTableVar,$2) == 1)
                        fprintf(f,"\twritef\n");
                    }
       | ENVIA STR  {
                      fprintf(f,"\tpushs \%s\n", $2); 
                      fprintf(f,"\twrites\n");
                    }      
       ;

Input : RECEBE ID { if(get_HashTable(hashTableVar,$2)!=NULL){
                      fprintf(f,"\tread\n");
                      if(getType(hashTableVar,$2) == 0){
                        fprintf(f,"\tatoi\n");
                        
                      }
                      if(getType(hashTableVar,$2) == 1){
                        fprintf(f,"\tatof\n");
                       
                      }
                      fprintf(f,"\tstoreg %d\n",getEndereco(hashTableVar,$2));
                      } else
                      {
                      erroDeclaracaow(numeroLinha,$2);
                    }
                  }
      ;



%%

#include "lex.yy.c"


void insereVariavel(HashTable hashTableVar, char *variavel, int tipo){  
  table existe = get_HashTable(hashTableVar, variavel);
  if(existe!=NULL) {
                        char *aux = (char*)malloc(sizeof(aux)+1);
                        sprintf(aux,"%d",numeroLinha);
                        strcat(erros,"Erro de Declaração na linha ");
                        strcat(erros, aux); 
                        strcat(erros, ": Já existe uma variável com o nome "); 
                        strcat(erros,"\"");
                        strcat(erros,variavel);
                        strcat(erros,"\".\n");
                        strcat(erros, "Sugerimos escolher um nome diferente para a variavel "); 

                   }
      
  if(existe==NULL) 
      {

          hashTableVar=addHashTable(hashTableVar, variavel, countVar, type);
          countVar++;
          if(tipo == 0)
            fprintf(f,"pushi 0\n");
          if(tipo == 1)
            fprintf(f,"pushf 0.0\n");
      }
}




void erroAtribuicao(int numeroLinha, char *variavel){
    char *aux = (char*)malloc(sizeof(aux)+1); sprintf(aux,"%d",numeroLinha);
    strcat(erros,"Erro de atribuiçao na linha "); strcat(erros, aux);
    strcat(erros, ": A seguinte variavel nao foi inicializada: ");
    strcat(erros,"\"");
    strcat(erros,variavel);
    strcat(erros,"\".\n");
}

void erroDeclaracaow(int numeroLinha, char *variavel)
{
  char *aux = (char*)malloc(sizeof(aux)+1); sprintf(aux,"%d",numeroLinha);
  strcat(erros,"Erro de Declaraçao na linha ");
  strcat(erros, aux);
  strcat(erros, ": A seguinte variavel não foi declarada: "); strcat(erros,"\"");
  strcat(erros,variavel);
  strcat(erros,"\".\n");
}








int yyerror(char *s)
{
  fprintf(stderr, "ERRO: %s \n", s);
}

int main()
{
f = fopen("assembly_code.vm","w");
hashTableVar = createHashTable(0);
yyparse();
fclose(f);


return 0; 
}

