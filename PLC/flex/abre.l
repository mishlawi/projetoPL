%{
/* Declarações C diversas */
%}

%%
[a-z| A-Z]  { printf("%s", yytext); }
"\mmm" { printf("mesmo") ;}
"\mt" {printf("muito") ;}
"b." {printf("boa.");}
"\n" {printf("\n");}
"na" {printf("Na");}
"\prox" {printf("próxima");}
"\mm" {printf("mesmo") ;}
"nao" {printf("não");}
"4/5" {printf("4/5") ;}
"~" {printf("in") ;}
"queixar-se" {printf("queixar-se") ;}
"\exs" {printf("exercicios") ;}
"\pq/" {printf("porque") ;}
"responder" {printf("responder") ;}
"\cqd" {printf("como queriamos demonstrar") ;}
"~=" {printf ("~=") ;}
"não" {printf ("não") ;}
"é" {printf("é") ;}
"sp" {printf("sempre") ;}
"!" {printf("!") ;}
"/" {printf("mente") ;}


(.|\n)  { ; } 
%%

int yywrap() {
    
    return(1);
}

int main() {

    yylex();
    return(0);
}