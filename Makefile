CC=gcc
CFLAGS=-fno-stack-protector -z execstack -no-pie -w

all: chal1 chal2 chal3

chal1: chal1.c
	$(CC) $(CFLAGS) -o chal1 chal1.c

chal2: chal2.c
	$(CC) $(CFLAGS) -o chal2 chal2.c

chal3: chal3.c
	$(CC) $(CFLAGS) -o chal chal3.c

clean:
	rm -f chal1
