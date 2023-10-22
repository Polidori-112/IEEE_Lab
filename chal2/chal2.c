#include <stdlib.h>
#include <stdio.h>

void win() {
	//Following code prints out file flag.txt
    FILE *file = fopen("flag.txt", "r"); // Open the file in read mode
    if (file == NULL) {
        printf("Error: Could not open flag.txt\n");
        return;
    }
    char ch;
    while ((ch = fgetc(file)) != EOF) { // Read characters one by one until End Of File (EOF)
        	putchar(ch); // Print the character      	
    }
    fclose(file); // Close the file
}

int main() {

	char buf[20];
	

	printf("What is your name?\n");
	gets(buf);

	printf("Hi %s, can you figure out how to win?\n", buf);

	return 0;
}
