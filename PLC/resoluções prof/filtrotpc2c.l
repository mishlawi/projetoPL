%{
#include <string.h>
#include <stdlib.h>
#define TEMPO "[TMP]Emplastro"

char *eu; 
char *ele;
int i;
%}

LETRA	[a-zA-Z]	
%x DEFeu DEFele

%%
^(?i:eu)[ ]*\=[ ]*      { BEGIN DEFeu; }
<DEFeu>\n               { BEGIN INITIAL; }
<DEFeu>.+               { eu = strdup(yytext); }
^(?i:ele)[ ]*\=[ ]*     { BEGIN DEFele; }
<DEFele>\n              { BEGIN INITIAL; }
<DEFele>.+              { ele = strdup(yytext); }
^(?i:eu)[ ]*\:		    { printf("%s:", eu); }
^(?i:e
le)[ ]*\:	        { printf("%s:", ele); }	 
%%
int yywrap() 
{
	return(1);
}

int main() 
{
    eu = strdup(TEMPO);
    ele = strdup(TEMPO);
	yylex();
	free(eu);
	free(ele);
	return(0);
}
