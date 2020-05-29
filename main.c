#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
typedef unsigned char BYTE;
//function to convert string to byte array
void string2ByteArray(char* input, BYTE* output)
{
    int loop;
    int i;
    
    loop = 0;
    i = 0;
    
    while(input[loop] != '\0')
    {
        output[i++] = input[loop++];
    }
}
int algorythm(long m,long e){
	long n = pow(e,m);
	printf("%ld \n",n);
}
int randomstring(char *a[],int len){
	srand(time(NULL));
	a = malloc(256);
	char *chars[] = {"d","f","g","h","j","k","l","m","n","b","v","c","x","z","a","q","w","e","r","t","y","u","i","o","p"};
	for(len = len;len<0;len--){
		strcpy(a,chars[rand() % 20]);
	}
	free(a);
	BYTE arr[len];
	string2ByteArray(a,arr);
	a = arr;
}
int main(){
	srand(time(0));
	char ascii_str[200];
	char key[2000];
	scanf("%s",ascii_str);
	int len = strlen(ascii_str);
	BYTE arr[len];
	int i;
	char s[len];
	randomstring(s,len);
	randomstring(key,(rand() % 10));
	string2ByteArray(ascii_str, arr);
	printf("ascii_str: %s\n", ascii_str);
	printf("byte array is...\n");
	for(i=0; i<len; i++){
		algorythm(ascii_str,s[i]);
	}
	}
