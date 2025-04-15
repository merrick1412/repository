%{
/*
name: merrick moncure  
assignment: cop4342 - assignment 10  
file: cpretty.l  
purpose: pretty print c code using groff formatting
*/

#include <stdio.h>
#include <string.h>

// list of c reserved words
char *reserved[] = {
  "auto", "break", "case", "char", "const", "continue", "default", "do",
  "double", "else", "enum", "extern", "float", "for", "goto", "if", "int",
  "long", "register", "return", "short", "signed", "sizeof", "static",
  "struct", "switch", "typedef", "union", "unsigned", "void", "volatile",
  "while", 0
};

// check if a word is reserved
int is_reserved(const char *word) {
  int i;
  for (i = 0; reserved[i] != 0; i++) {
    if (strcmp(reserved[i], word) == 0)
      return 1;
  }
  return 0;
}
%}

%%

[/][*]              { printf("\\f(CI%s", yytext); }   // match start of comment
[*][/]              { printf("%s\\f(CR", yytext); }   // match end of comment
\/\/.*             { printf("\\f(CI%s\\f(CR", yytext); }   /* single-line comment */
\"[^\"\n]*\"       { printf("\\fB%s\\f(CR", yytext); }     /* string literal */
\'[^'\n]\'         { printf("\\fI%s\\f(CR", yytext); }     /* character literal */
[0-9]+             { printf("\\f5%s\\f(CR", yytext); }     /* integer */
[a-zA-Z_][a-zA-Z0-9_]* {
                      if (is_reserved(yytext))
                        printf("\\f(CB%s\\f(CR", yytext);  /* keyword */
                      else
                        printf("%s", yytext);              /* identifier */
                    }
[ \t]+             { printf("%s", yytext); }               /* whitespace */
\n                 { printf("\n"); }                       /* newline */
.                  { printf("%s", yytext); }               /* other */

%%

int main(void) {
  printf(".fp 5 cbi\n");  /* define courier bold oblique */
  printf(".ft cr\n");     /* default to courier */
  printf(".nf\n");        /* disable line filling */
  yylex();
  return 0;
}
