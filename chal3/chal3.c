#include <stdlib.h>
#include <stdio.h>

int main() {

	char buf[20];
	

	printf("What is your name?\n");
	gets(buf);

	printf("Hi %s, can you figure out how to win?\n", buf);

	return 0;
}
