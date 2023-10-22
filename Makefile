CC=gcc
CFLAGS=-fno-stack-protector -z execstack -no-pie -w

all: chal1 chal2

chal1: chal1.c
	$(CC) $(CFLAGS) -o chal1 chal1.c

chal2: chal2.c
	$(CC) $(CFLAGS) -o chal2 chal2.c

clean:
	rm -f chal1
