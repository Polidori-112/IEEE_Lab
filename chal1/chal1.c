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
	long int secret_number = 0;
	

	printf("What is your name?\n");
	gets(buf);

	printf("Hi %s, can you figure out how to win?\n", buf);

	if (secret_number == 42) {
		printf("Congrats, you found it!!\n");
		win();
	}

	else if (secret_number != 0) { 
		printf("Huh, how did you do that? My secret number is now %ld (0x%lx)\n", secret_number, secret_number);
	}
		
	return 0;
}
