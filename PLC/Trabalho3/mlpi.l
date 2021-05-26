%{
#include "y.tab.h"
#include "hashtable.h"
#include "stack.h"
%}

%%
[=+\-*/()><!,:;{}]          { return yytext[0]; }
[TtFf]                     {yylval.valb=strdup(yytext); return NBOOL; }
INTEIRO                   {return INTEIRO;}
REAL                      {return REAL;}
BOOL                      {return BOOL;}
SE                        {return SE;}
SENAO                     {return SENAO;}
ENQUANTO                  {return ENQUANTO;}
INICIO                    {return INICIO;}
FIM                       {return FIM;}
ENVIA                     {return ENVIA;}
RECEBE                    {return RECEBE;}
[a-zA-Z][a-zA-Z0-9]*      { yylval.vals=strdup(yytext); return ID; }
[0-9]+                    { yylval.vali=atoi(yytext); return NUMI; }
[+-]?([0-9]*[.])?[0-9]+   { yylval.valf=atof(yytext);  return NUMF; }
\"[^"]+\"              { yylval.vals = strdup(yytext);return STR;}





.|\n                  { ; }

%%
int yywrap()
{ return(1); }
