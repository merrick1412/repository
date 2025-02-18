/*************************************************************************
 * 12/31/2016                                                            *
 * shell.c was downloaded from MTU:                                      *
 * http://www.csl.mtu.edu/cs4411.ck/www/NOTES/process/fork/exec.html     *
 *                                                                       *
 * NOTE: The original code has quite ugly parse() routine with dangerous *
 * library routine gets(). To address these deficiences, I (Gang-Ryung)  *
 * rewrote main() and parse() routine using fgets and strtok.            *
 *************************************************************************/

/* ----------------------------------------------------------------- */
/* PROGRAM  shell.c                                                  */
/*    This program reads in an input line, parses the input line     */
/* into tokens, and use execvp() to execute the command.             */
/* ----------------------------------------------------------------- */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>
#include <ctype.h>

//sorry, I cant test this without using readline or ill rip my hair out


extern FILE *stdin;
extern FILE *stdout;
extern FILE *stderr;

/* ----------------------------------------------------------------- */
/* FUNCTION  parse:                                                  */
/*    This function takes an input line and parse it into tokens.    */
/* It first replaces all white spaces with zeros until it hits a     */
/* non-white space character which indicates the beginning of an     */
/* argument.  It saves the address to argv[], and then skips all     */
/* non-white spaces which constitute the argument.                   */
/* ----------------------------------------------------------------- */

void  parse(char *line, char **argv)
{
    static char* delimiter = " \n\t";
    char *token = strtok(line, delimiter);
    while (token != NULL) {
        if (strlen(token) > 0){ //ignores empty tokens
            *argv++ = token;
        }

        token = strtok(NULL, delimiter);
    }
    *argv = (char *)'\0';                 /* mark the end of argument list  */
}

/* ----------------------------------------------------------------- */
/* FUNCTION execute:                                                 */
/*    This function receives a commend line argument list with the   */
/* first one being a file name followed by its arguments.  Then,     */
/* this function forks a child process to execute the command using  */
/* system call execvp().                                             */
/* ----------------------------------------------------------------- */

void  execute(char **argv)
{


    pid_t  pid = fork();
    int    status;

    if (pid < 0) {     /* fork a child process           */
        printf("*** ERROR: forking child process failed\n");
        exit(1);
    }
    else if (pid == 0) {          /* for the child process:         */
        if (execvp(*argv, argv) < 0) {     /* execute the command  */
            printf("*** ERROR: exec failed\n");
            exit(1);
        }
    }
    else {                                  /* for the parent:      */
        while (wait(&status) != pid)       /* wait for completion  */
            ;
    }
}

void handleBatch(char *filename){
    FILE *file = fopen(filename, "r");
    if (file == NULL){
        fprintf(stderr, "cant open batch file: %s\n",filename);
        exit(1);
    }
    char line [1024];
    while (fgets(line,sizeof(line),file)){
        //deal with whitespace
        line[strcspn(line,"\n")] = '\0';
        char *command = strtok(line, ";");

        while (command != NULL){//trimming whitespace
            while (isspace((unsigned char)*command)) command++; //remoce leading spaces
            char *end = command + strlen(command) -1;
            while (end > command && isspace((unsigned char)*end)) end--; //remove trailing spaces
            *(end + 1) = '\0'; //ensure its null terminated

            if (strlen(command) > 0){
                //parse into args
                char *argv[64];
                parse(line,argv);
                if (argv[0] == NULL){
                    command = strtok(NULL,";");
                    continue; //skip empty commands
                }

                if (strcmp(argv[0],"quit") == 0){
                    exit(0);
                    fclose(file); //in case quit
                    return;
                }
                execute(argv);
            }
            command = strtok(NULL, ";"); //move to the next command
        }
    }
    fclose(file);
 }

/* ----------------------------------------------------------------- */
/*                  The main program starts here                     */
/* ----------------------------------------------------------------- */

int main(int argc, char *argv[])
{
    if (argc == 2) {//batch
        handleBatch(argv[1]);
    }
    else if (argc == 1) { //interactive mode


        char line[1024];             /* the input line                 */
        char *argv[64];              /* the command line argument      */
        //char *c = NULL;


        printf("Shell -> ");          /*   display a prompt             */


        while (fgets(line, sizeof(line), stdin)) {
            /* repeat until EOF .... */
            char *commands[64];
            char *command = strtok(line, ";");
            int command_count = 0;

            while (command != NULL){
                commands[command_count++] = command;
                command = strtok(NULL,";");
            }
            for (int i = 0; i < command_count; i++){
                char *command_line = commands[i];
                parse(command_line, argv);

                if (argv[0] == NULL){ //skip empty commands, like ;;
                    continue;
                }
                if(strcmp(argv[0],"quit") == 0){
                    exit(0);
                }
                execute(argv);
            }
            printf("Shell -> ");       /*   display a prompt             */
        }
    }
    else{
        //too many args
        fprintf(stderr, "Usage: %s [batchfile]\n", argv[0]);
        exit(1);
    }

    return 0;
}


