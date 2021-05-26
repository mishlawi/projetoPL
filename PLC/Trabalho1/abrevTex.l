%{

#include <string.h>
#include <stdlib.h>


%}


%s topicoitem topiconum topicodic centrar
%option stack





%%

\\ng {printf("\\textbf");}

\\it {printf("\\textit"); }

\\sub {printf("\\underline"); }

^\\sec {printf("\\section"); }

^\\ssec {printf("\\subsection"); }

^\\cap {printf("\\chapter"); }

\\np {printf("\\newpage");}

^"-" {printf("\\item %s", yytext + 1);}



^:C\{ {BEGIN(centrar); printf("\\begin{center}");yy_push_state(centrar);}
<centrar>(:C\}) {printf("\\end{center}");yy_pop_state();}



^":I\{" BEGIN topicoitem;{printf("\\begin{itemize}"); yy_push_state(topicoitem);}
<topicoitem>(:I\}) { printf("\\end{itemize}" ); yy_pop_state(); BEGIN(0);}




^":N\{" {BEGIN topiconum ; printf("\\begin{enumerate}"); yy_push_state(topiconum);}
<topiconum>(:N\}) {printf ("\\end{enumerate}"); yy_pop_state(); BEGIN (INITIAL); }


^":D\{" {BEGIN topicodic ; printf("\\begin{description}");  yy_push_state(topicodic);}
<topicodic>(:D\}) {printf("\\end{description}"); yy_pop_state(); BEGIN (INITIAL);}




%%

void begintex () {
    printf("\\documentclass{report}\n\\usepackage[portuguese]{babel}\n\\usepackage[utf8]{inputenc}\n\\begin{document}\n" );
}

void endtex () {
    printf("\\end{document}\n" );
}

int yywrap() {
    
    return(1);
}

int main (){

    begintex();
    yylex();
    endtex();
    return 0;
}