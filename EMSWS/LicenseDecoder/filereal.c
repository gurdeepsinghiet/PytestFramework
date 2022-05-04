#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "licensing.h"
#include "licgen_parser.h"
char *readLine(FILE *fp);
char *fileDecode();
int main(){
      FILE* fp;
      FILE* fptw;
        char *pcBuffer = NULL;
         int lineCount = 0 ;
           char *pcOutBuffer= NULL;
            int rc = -1;
     fp = fopen("lservrc", "r+");
       fptw = fopen("licdododer.txt", "w+");
      while ((pcBuffer = readLine(fp)) != NULL) {
              if ((pcBuffer[0] == '\0') || (pcBuffer[0] == '\n') || (pcBuffer[0] == '#')) {
                /* Skip the empty line*/
                ++lineCount;
            }else {
                printf("Decoding of License String : ");
                rc =sntl_licgen_parse(NULL, pcBuffer, &pcOutBuffer);
                  fputs(pcOutBuffer, fptw);
                      printf("Successful\n");
                      printf("License Information:\n===============\n%s===============\n", pcOutBuffer);
                      printf("\n");
                      //sntl_licensing_free(pcOutBuffer);
                      
               
          }
    printf("ngngngngn");
    return 0;
}
fileDecode();
}

char *fileDecode(){
     FILE* fp;
     FILE *fptw;
     
        char *pcBuffer = NULL;
         int lineCount = 0 ;
           char *pcOutBuffer= NULL;
            int rc = -1;
      fp = fopen("lservrc", "r+");
      fptw = fopen("licdododer.txt", "w+");
      while ((pcBuffer = readLine(fp)) != NULL) {
              if ((pcBuffer[0] == '\0') || (pcBuffer[0] == '\n') || (pcBuffer[0] == '#')) {
                /* Skip the empty line*/
                ++lineCount;
            }else {
                printf("Decoding of License String : ");
                rc =sntl_licgen_parse(NULL, pcBuffer, &pcOutBuffer);
                 fputs(pcOutBuffer, fptw);
                      printf("Successful\n");
                      printf("License Information:\n===============\n%s===============\n", pcOutBuffer);
                      printf("\n");
                      //sntl_licensing_free(pcOutBuffer);
                      
               
          }
    printf("ngngngngn");
    fclose(fp);
    fclose(fptw);
    return (pcOutBuffer);
}
}

char *readLine(FILE *fp) 
{
    int maximumLineLength = 128;
    char *pcLineBuffer = NULL;
    int ch = 0;
    int count = 0;

    ch = getc(fp);
    if (ch == EOF) {
       return NULL;
    }

    pcLineBuffer = (char *)malloc(sizeof(char) * maximumLineLength);
    if (pcLineBuffer == NULL) {
        printf("Failure - Error allocating memory for pcBuffer pcBuffer.\n");
        return NULL;
    }

    while ((ch != '\n') && (ch != EOF)) {
        if (count == maximumLineLength-1) {
            maximumLineLength += 128;
            pcLineBuffer = realloc(pcLineBuffer, maximumLineLength);
            if (pcLineBuffer == NULL) {
                printf("Failure - Error reallocating space for pcBuffer pcBuffer.\n");
                return NULL;
            }
        }
        pcLineBuffer[count] = ch;
        count++;
        ch = getc(fp);
    }
    pcLineBuffer[count] = '\0';
    return pcLineBuffer;
}


char *readLining() 
{

     FILE* fp;
     fp = fopen("lservrc", "r+");
    int maximumLineLength = 128;
    char *pcLineBuffer = NULL;
    int ch = 0;
    int count = 0;

    ch = getc(fp);
    if (ch == EOF) {
       return NULL;
    }

    pcLineBuffer = (char *)malloc(sizeof(char) * maximumLineLength);
    if (pcLineBuffer == NULL) {
        printf("Failure - Error allocating memory for pcBuffer pcBuffer.\n");
        return NULL;
    }

    while ((ch != '\n') && (ch != EOF)) {
        if (count == maximumLineLength-1) {
            maximumLineLength += 128;
            pcLineBuffer = realloc(pcLineBuffer, maximumLineLength);
            if (pcLineBuffer == NULL) {
                printf("Failure - Error reallocating space for pcBuffer pcBuffer.\n");
                return NULL;
            }
        }
        pcLineBuffer[count] = ch;
        count++;
        ch = getc(fp);
    }
    pcLineBuffer[count] = '\0';
    return pcLineBuffer;
}