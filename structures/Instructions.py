#http://en.wikipedia.org/wiki/Java_bytecode_instruction_listings
import struct

def MakeInstruction(code, arg_pack=""):
    class Instruction:
        def __init__(self, *args):
            self.arg_list = list(args)
        def dump(self, cp):
            arg_vals = map(cp.get, self.arg_list)
            return struct.pack(">B"+arg_pack, code, *arg_vals)
    return Instruction

# load onto the stack a reference from an array
#  arrayref, index &#8594; value 
aaload = MakeInstruction(0x32)

# store into a reference in an array
#  arrayref, index, value &#8594; 
aastore = MakeInstruction(0x53)

# push a ''null'' reference onto the stack
#  &#8594; null 
aconst_null = MakeInstruction(0x01)

# load a reference onto the stack from a local variable ''#index''
#  &#8594; objectref 
aload = MakeInstruction(0x19,'B')

# load a reference onto the stack from local variable 0
#  &#8594; objectref 
aload_0 = MakeInstruction(0x2a)

# load a reference onto the stack from local variable 1
#  &#8594; objectref 
aload_1 = MakeInstruction(0x2b)

# load a reference onto the stack from local variable 2
#  &#8594; objectref 
aload_2 = MakeInstruction(0x2c)

# load a reference onto the stack from local variable 3
#  &#8594; objectref 
aload_3 = MakeInstruction(0x2d)

# create a new array of references of length ''count'' and component typ
# e identified by the class reference ''index'' (''indexbyte1 &lt;&lt; 8
#  + indexbyte2'') in the constant pool
#  count &#8594; arrayref 
anewarray = MakeInstruction(0xbd,'H')

# return a reference from a method
#  objectref &#8594; [empty] 
areturn = MakeInstruction(0xb0)

# get the length of an array
#  arrayref &#8594; length 
arraylength = MakeInstruction(0xbe)

# store a reference into a local variable ''#index''
#  objectref &#8594; 
astore = MakeInstruction(0x3a,'B')

# store a reference into local variable 0
#  objectref &#8594; 
astore_0 = MakeInstruction(0x4b)

# store a reference into local variable 1
#  objectref &#8594; 
astore_1 = MakeInstruction(0x4c)

# store a reference into local variable 2
#  objectref &#8594; 
astore_2 = MakeInstruction(0x4d)

# store a reference into local variable 3
#  objectref &#8594; 
astore_3 = MakeInstruction(0x4e)

# throws an error or exception (notice that the rest of the stack is cle
# ared, leaving only a reference to the Throwable)
#  objectref &#8594; [empty], objectref 
athrow = MakeInstruction(0xbf)

# load a byte or Boolean value from an array
#  arrayref, index &#8594; value 
baload = MakeInstruction(0x33)

# store a byte or Boolean value into an array
#  arrayref, index, value &#8594; 
bastore = MakeInstruction(0x54)

# push a ''byte'' onto the stack as an integer ''value''
#  &#8594; value 
bipush = MakeInstruction(0x10,'B')

# reserved for breakpoints in Java debuggers; should not appear in any c
# lass file
#  
breakpoint = MakeInstruction(0xca)

# load a char from an array
#  arrayref, index &#8594; value 
caload = MakeInstruction(0x34)

# store a char into an array
#  arrayref, index, value &#8594; 
castore = MakeInstruction(0x55)

# checks whether an ''objectref'' is of a certain type, the class refere
# nce of which is in the constant pool at ''index'' (''indexbyte1 &lt;&l
# t; 8 + indexbyte2'')
#  objectref &#8594; objectref 
checkcast = MakeInstruction(0xc0,'H')

# convert a double to a float
#  value &#8594; result 
d2f = MakeInstruction(0x90)

# convert a double to an int
#  value &#8594; result 
d2i = MakeInstruction(0x8e)

# convert a double to a long
#  value &#8594; result 
d2l = MakeInstruction(0x8f)

# add two doubles
#  value1, value2 &#8594; result 
dadd = MakeInstruction(0x63)

# load a double from an array
#  arrayref, index &#8594; value 
daload = MakeInstruction(0x31)

# store a double into an array
#  arrayref, index, value &#8594; 
dastore = MakeInstruction(0x52)

# compare two doubles
#  value1, value2 &#8594; result 
dcmpg = MakeInstruction(0x98)

# compare two doubles
#  value1, value2 &#8594; result 
dcmpl = MakeInstruction(0x97)

# push the constant ''0.0'' onto the stack
#  &#8594; 0.0 
dconst_0 = MakeInstruction(0x0e)

# push the constant ''1.0'' onto the stack
#  &#8594; 1.0 
dconst_1 = MakeInstruction(0x0f)

# divide two doubles
#  value1, value2 &#8594; result 
ddiv = MakeInstruction(0x6f)

# load a double ''value'' from a local variable ''#index''
#  &#8594; value 
dload = MakeInstruction(0x18,'B')

# load a double from local variable 0
#  &#8594; value 
dload_0 = MakeInstruction(0x26)

# load a double from local variable 1
#  &#8594; value 
dload_1 = MakeInstruction(0x27)

# load a double from local variable 2
#  &#8594; value 
dload_2 = MakeInstruction(0x28)

# load a double from local variable 3
#  &#8594; value 
dload_3 = MakeInstruction(0x29)

# multiply two doubles
#  value1, value2 &#8594; result 
dmul = MakeInstruction(0x6b)

# negate a double
#  value &#8594; result 
dneg = MakeInstruction(0x77)

# get the remainder from a division between two doubles
#  value1, value2 &#8594; result 
drem = MakeInstruction(0x73)

# return a double from a method
#  value &#8594; [empty] 
dreturn = MakeInstruction(0xaf)

# store a double ''value'' into a local variable ''#index''
#  value &#8594; 
dstore = MakeInstruction(0x39,'B')

# store a double into local variable 0
#  value &#8594; 
dstore_0 = MakeInstruction(0x47)

# store a double into local variable 1
#  value &#8594; 
dstore_1 = MakeInstruction(0x48)

# store a double into local variable 2
#  value &#8594; 
dstore_2 = MakeInstruction(0x49)

# store a double into local variable 3
#  value &#8594; 
dstore_3 = MakeInstruction(0x4a)

# subtract a double from another
#  value1, value2 &#8594; result 
dsub = MakeInstruction(0x67)

# duplicate the value on top of the stack
#  value &#8594; value, value 
dup = MakeInstruction(0x59)

# insert a copy of the top value into the stack two values from the top.
#  value1 and value2 must not be of the type double or long.
#  value2, value1 &#8594; value1, value2, value1 
dup_x1 = MakeInstruction(0x5a)

# insert a copy of the top value into the stack two (if value2 is double
#  or long it takes up the entry of value3, too) or three values (if val
# ue2 is neither double nor long) from the top
#  value3, value2, value1 &#8594; value1, value3, value2, value1 
dup_x2 = MakeInstruction(0x5b)

# duplicate top two stack words (two values, if value1 is not double nor
#  long; a single value, if value1 is double or long)
#  {value2, value1} &#8594; {value2, value1}, {value2, value1} 
dup2 = MakeInstruction(0x5c)

# duplicate two words and insert beneath third word (see explanation abo
# ve)
#  value3, {value2, value1} &#8594; {value2, value1}, value3, {value2, value1} 
dup2_x1 = MakeInstruction(0x5d)

# duplicate two words and insert beneath fourth word
#  {value4, value3}, {value2, value1} &#8594; {value2, value1}, {value4, value3}, {value2, value1} 
dup2_x2 = MakeInstruction(0x5e)

# convert a float to a double
#  value &#8594; result 
f2d = MakeInstruction(0x8d)

# convert a float to an int
#  value &#8594; result 
f2i = MakeInstruction(0x8b)

# convert a float to a long
#  value &#8594; result 
f2l = MakeInstruction(0x8c)

# add two floats
#  value1, value2 &#8594; result 
fadd = MakeInstruction(0x62)

# load a float from an array
#  arrayref, index &#8594; value 
faload = MakeInstruction(0x30)

# store a float in an array
#  arrayref, index, value &#8594; 
fastore = MakeInstruction(0x51)

# compare two floats
#  value1, value2 &#8594; result 
fcmpg = MakeInstruction(0x96)

# compare two floats
#  value1, value2 &#8594; result 
fcmpl = MakeInstruction(0x95)

# push ''0.0f'' on the stack
#  &#8594; 0.0f 
fconst_0 = MakeInstruction(0x0b)

# push ''1.0f'' on the stack
#  &#8594; 1.0f 
fconst_1 = MakeInstruction(0x0c)

# push ''2.0f'' on the stack
#  &#8594; 2.0f 
fconst_2 = MakeInstruction(0x0d)

# divide two floats
#  value1, value2 &#8594; result 
fdiv = MakeInstruction(0x6e)

# load a float ''value'' from a local variable ''#index''
#  &#8594; value 
fload = MakeInstruction(0x17,'B')

# load a float ''value'' from local variable 0
#  &#8594; value 
fload_0 = MakeInstruction(0x22)

# load a float ''value'' from local variable 1
#  &#8594; value 
fload_1 = MakeInstruction(0x23)

# load a float ''value'' from local variable 2
#  &#8594; value 
fload_2 = MakeInstruction(0x24)

# load a float ''value'' from local variable 3
#  &#8594; value 
fload_3 = MakeInstruction(0x25)

# multiply two floats
#  value1, value2 &#8594; result 
fmul = MakeInstruction(0x6a)

# negate a float
#  value &#8594; result 
fneg = MakeInstruction(0x76)

# get the remainder from a division between two floats
#  value1, value2 &#8594; result 
frem = MakeInstruction(0x72)

# return a float
#  value &#8594; [empty] 
freturn = MakeInstruction(0xae)

# store a float ''value'' into a local variable ''#index''
#  value &#8594; 
fstore = MakeInstruction(0x38,'B')

# store a float ''value'' into local variable 0
#  value &#8594; 
fstore_0 = MakeInstruction(0x43)

# store a float ''value'' into local variable 1
#  value &#8594; 
fstore_1 = MakeInstruction(0x44)

# store a float ''value'' into local variable 2
#  value &#8594; 
fstore_2 = MakeInstruction(0x45)

# store a float ''value'' into local variable 3
#  value &#8594; 
fstore_3 = MakeInstruction(0x46)

# subtract two floats
#  value1, value2 &#8594; result 
fsub = MakeInstruction(0x66)

# get a field ''value'' of an object ''objectref'', where the field is i
# dentified by field reference in the constant pool ''index'' (''index1 
# &lt;&lt; 8 + index2'')
#  objectref &#8594; value 
getfield = MakeInstruction(0xb4,'H')

# get a static field ''value'' of a class, where the field is identified
#  by field reference in the constant pool ''index'' (''index1 &lt;&lt; 
# 8 + index2'')
#  &#8594; value 
getstatic = MakeInstruction(0xb2,'H')

# goes to another instruction at ''branchoffset'' (signed short construc
# ted from unsigned bytes ''branchbyte1 &lt;&lt; 8 + branchbyte2'')
#  [no change] 
goto = MakeInstruction(0xa7,'H')

# goes to another instruction at ''branchoffset'' (signed int constructe
# d from unsigned bytes ''branchbyte1 &lt;&lt; 24 + ''branchbyte2 &lt;&l
# t; 16 + ''branchbyte3 &lt;&lt; 8 + branchbyte4'')
#  [no change] 
goto_w = MakeInstruction(0xc8,'L')

# convert an int into a byte
#  value &#8594; result 
i2b = MakeInstruction(0x91)

# convert an int into a character
#  value &#8594; result 
i2c = MakeInstruction(0x92)

# convert an int into a double
#  value &#8594; result 
i2d = MakeInstruction(0x87)

# convert an int into a float
#  value &#8594; result 
i2f = MakeInstruction(0x86)

# convert an int into a long
#  value &#8594; result 
i2l = MakeInstruction(0x85)

# convert an int into a short
#  value &#8594; result 
i2s = MakeInstruction(0x93)

# add two ints
#  value1, value2 &#8594; result 
iadd = MakeInstruction(0x60)

# load an int from an array
#  arrayref, index &#8594; value 
iaload = MakeInstruction(0x2e)

# perform a bitwise and on two integers
#  value1, value2 &#8594; result 
iand = MakeInstruction(0x7e)

# store an int into an array
#  arrayref, index, value &#8594; 
iastore = MakeInstruction(0x4f)

# load the int value -1 onto the stack
#  &#8594; -1 
iconst_m1 = MakeInstruction(0x02)

# load the int value 0 onto the stack
#  &#8594; 0 
iconst_0 = MakeInstruction(0x03)

# load the int value 1 onto the stack
#  &#8594; 1 
iconst_1 = MakeInstruction(0x04)

# load the int value 2 onto the stack
#  &#8594; 2 
iconst_2 = MakeInstruction(0x05)

# load the int value 3 onto the stack
#  &#8594; 3 
iconst_3 = MakeInstruction(0x06)

# load the int value 4 onto the stack
#  &#8594; 4 
iconst_4 = MakeInstruction(0x07)

# load the int value 5 onto the stack
#  &#8594; 5 
iconst_5 = MakeInstruction(0x08)

# divide two integers
#  value1, value2 &#8594; result 
idiv = MakeInstruction(0x6c)

# if references are equal, branch to instruction at ''branchoffset'' (si
# gned short constructed from unsigned bytes ''branchbyte1 &lt;&lt; 8 + 
# branchbyte2'')
#  value1, value2 &#8594; 
if_acmpeq = MakeInstruction(0xa5,'H')

# if references are not equal, branch to instruction at ''branchoffset''
#  (signed short constructed from unsigned bytes ''branchbyte1 &lt;&lt; 
# 8 + branchbyte2'')
#  value1, value2 &#8594; 
if_acmpne = MakeInstruction(0xa6,'H')

# if ints are equal, branch to instruction at ''branchoffset'' (signed s
# hort constructed from unsigned bytes ''branchbyte1 &lt;&lt; 8 + branch
# byte2'')
#  value1, value2 &#8594; 
if_icmpeq = MakeInstruction(0x9f,'H')

# if ''value1'' is greater than or equal to ''value2'', branch to instru
# ction at ''branchoffset'' (signed short constructed from unsigned byte
# s ''branchbyte1 &lt;&lt; 8 + branchbyte2'')
#  value1, value2 &#8594; 
if_icmpge = MakeInstruction(0xa2,'H')

# if ''value1'' is greater than ''value2'', branch to instruction at ''b
# ranchoffset'' (signed short constructed from unsigned bytes ''branchby
# te1 &lt;&lt; 8 + branchbyte2'')
#  value1, value2 &#8594; 
if_icmpgt = MakeInstruction(0xa3,'H')

# if ''value1'' is less than or equal to ''value2'', branch to instructi
# on at ''branchoffset'' (signed short constructed from unsigned bytes '
# 'branchbyte1 &lt;&lt; 8 + branchbyte2'')
#  value1, value2 &#8594; 
if_icmple = MakeInstruction(0xa4,'H')

# if ''value1'' is less than ''value2'', branch to instruction at ''bran
# choffset'' (signed short constructed from unsigned bytes ''branchbyte1
#  &lt;&lt; 8 + branchbyte2'')
#  value1, value2 &#8594; 
if_icmplt = MakeInstruction(0xa1,'H')

# if ints are not equal, branch to instruction at ''branchoffset'' (sign
# ed short constructed from unsigned bytes ''branchbyte1 &lt;&lt; 8 + br
# anchbyte2'')
#  value1, value2 &#8594; 
if_icmpne = MakeInstruction(0xa0,'H')

# if ''value'' is 0, branch to instruction at ''branchoffset'' (signed s
# hort constructed from unsigned bytes ''branchbyte1 &lt;&lt; 8 + branch
# byte2'')
#  value &#8594; 
ifeq = MakeInstruction(0x99,'H')

# if ''value'' is greater than or equal to 0, branch to instruction at '
# 'branchoffset'' (signed short constructed from unsigned bytes ''branch
# byte1 &lt;&lt; 8 + branchbyte2'')
#  value &#8594; 
ifge = MakeInstruction(0x9c,'H')

# if ''value'' is greater than 0, branch to instruction at ''branchoffse
# t'' (signed short constructed from unsigned bytes ''branchbyte1 &lt;&l
# t; 8 + branchbyte2'')
#  value &#8594; 
ifgt = MakeInstruction(0x9d,'H')

# if ''value'' is less than or equal to 0, branch to instruction at ''br
# anchoffset'' (signed short constructed from unsigned bytes ''branchbyt
# e1 &lt;&lt; 8 + branchbyte2'')
#  value &#8594; 
ifle = MakeInstruction(0x9e,'H')

# if ''value'' is less than 0, branch to instruction at ''branchoffset''
#  (signed short constructed from unsigned bytes ''branchbyte1 &lt;&lt; 
# 8 + branchbyte2'')
#  value &#8594; 
iflt = MakeInstruction(0x9b,'H')

# if ''value'' is not 0, branch to instruction at ''branchoffset'' (sign
# ed short constructed from unsigned bytes ''branchbyte1 &lt;&lt; 8 + br
# anchbyte2'')
#  value &#8594; 
ifne = MakeInstruction(0x9a,'H')

# if ''value'' is not null, branch to instruction at ''branchoffset'' (s
# igned short constructed from unsigned bytes ''branchbyte1 &lt;&lt; 8 +
#  branchbyte2'')
#  value &#8594; 
ifnonnull = MakeInstruction(0xc7,'H')

# if ''value'' is null, branch to instruction at ''branchoffset'' (signe
# d short constructed from unsigned bytes ''branchbyte1 &lt;&lt; 8 + bra
# nchbyte2'')
#  value &#8594; 
ifnull = MakeInstruction(0xc6,'H')

# increment local variable ''#index'' by signed byte ''const''
#  [No change] 
iinc = MakeInstruction(0x84,'H')

# load an int ''value'' from a local variable ''#index''
#  &#8594; value 
iload = MakeInstruction(0x15,'B')

# load an int ''value'' from local variable 0
#  &#8594; value 
iload_0 = MakeInstruction(0x1a)

# load an int ''value'' from local variable 1
#  &#8594; value 
iload_1 = MakeInstruction(0x1b)

# load an int ''value'' from local variable 2
#  &#8594; value 
iload_2 = MakeInstruction(0x1c)

# load an int ''value'' from local variable 3
#  &#8594; value 
iload_3 = MakeInstruction(0x1d)

# reserved for implementation-dependent operations within debuggers; sho
# uld not appear in any class file
#  
impdep1 = MakeInstruction(0xfe)

# reserved for implementation-dependent operations within debuggers; sho
# uld not appear in any class file
#  
impdep2 = MakeInstruction(0xff)

# multiply two integers
#  value1, value2 &#8594; result 
imul = MakeInstruction(0x68)

# negate int
#  value &#8594; result 
ineg = MakeInstruction(0x74)

# determines if an object ''objectref'' is of a given type, identified b
# y class reference ''index'' in constant pool (''indexbyte1 &lt;&lt; 8 
# + indexbyte2'')
#  objectref &#8594; result 
instanceof = MakeInstruction(0xc1,'H')

# invokes a dynamic method identified by method reference ''index'' in c
# onstant pool (''indexbyte1 &lt;&lt; 8 + indexbyte2'')
#  [arg1, [arg2 ...]] &#8594; 
invokedynamic = MakeInstruction(0xba,'L')

# invokes an interface method on object ''objectref'', where the interfa
# ce method is identified by method reference ''index'' in constant pool
#  (''indexbyte1 &lt;&lt; 8 + indexbyte2'')
#  objectref, [arg1, arg2, ...] &#8594; 
invokeinterface = MakeInstruction(0xb9,'L')

# invoke instance method on object ''objectref'', where the method is id
# entified by method reference ''index'' in constant pool (''indexbyte1 
# &lt;&lt; 8 + indexbyte2'')
#  objectref, [arg1, arg2, ...] &#8594; 
invokespecial = MakeInstruction(0xb7,'H')

# invoke a static method, where the method is identified by method refer
# ence ''index'' in constant pool (''indexbyte1 &lt;&lt; 8 + indexbyte2'
# ')
#  [arg1, arg2, ...] &#8594; 
invokestatic = MakeInstruction(0xb8,'H')

# invoke virtual method on object ''objectref'', where the method is ide
# ntified by method reference ''index'' in constant pool (''indexbyte1 &
# lt;&lt; 8 + indexbyte2'')
#  objectref, [arg1, arg2, ...] &#8594; 
invokevirtual = MakeInstruction(0xb6,'H')

# bitwise int or
#  value1, value2 &#8594; result 
ior = MakeInstruction(0x80)

# logical int remainder
#  value1, value2 &#8594; result 
irem = MakeInstruction(0x70)

# return an integer from a method
#  value &#8594; [empty] 
ireturn = MakeInstruction(0xac)

# int shift left
#  value1, value2 &#8594; result 
ishl = MakeInstruction(0x78)

# int arithmetic shift right
#  value1, value2 &#8594; result 
ishr = MakeInstruction(0x7a)

# store int ''value'' into variable ''#index''
#  value &#8594; 
istore = MakeInstruction(0x36,'B')

# store int ''value'' into variable 0
#  value &#8594; 
istore_0 = MakeInstruction(0x3b)

# store int ''value'' into variable 1
#  value &#8594; 
istore_1 = MakeInstruction(0x3c)

# store int ''value'' into variable 2
#  value &#8594; 
istore_2 = MakeInstruction(0x3d)

# store int ''value'' into variable 3
#  value &#8594; 
istore_3 = MakeInstruction(0x3e)

# int subtract
#  value1, value2 &#8594; result 
isub = MakeInstruction(0x64)

# int logical shift right
#  value1, value2 &#8594; result 
iushr = MakeInstruction(0x7c)

# int xor
#  value1, value2 &#8594; result 
ixor = MakeInstruction(0x82)

# jump to subroutine at ''branchoffset'' (signed short constructed from 
# unsigned bytes ''branchbyte1 &lt;&lt; 8 + branchbyte2'') and place the
#  return address on the stack
#  &#8594; address 
jsr = MakeInstruction(0xa8,'H')

# jump to subroutine at ''branchoffset'' (signed int constructed from un
# signed bytes ''branchbyte1 &lt;&lt; 24 + branchbyte2 &lt;&lt; 16 + bra
# nchbyte3 &lt;&lt; 8 + branchbyte4'') and place the return address on t
# he stack
#  &#8594; address 
jsr_w = MakeInstruction(0xc9,'L')

# convert a long to a double
#  value &#8594; result 
l2d = MakeInstruction(0x8a)

# convert a long to a float
#  value &#8594; result 
l2f = MakeInstruction(0x89)

# convert a long to a int
#  value &#8594; result 
l2i = MakeInstruction(0x88)

# add two longs
#  value1, value2 &#8594; result 
ladd = MakeInstruction(0x61)

# load a long from an array
#  arrayref, index &#8594; value 
laload = MakeInstruction(0x2f)

# bitwise and of two longs
#  value1, value2 &#8594; result 
land = MakeInstruction(0x7f)

# store a long to an array
#  arrayref, index, value &#8594; 
lastore = MakeInstruction(0x50)

# compare two longs values
#  value1, value2 &#8594; result 
lcmp = MakeInstruction(0x94)

# push the long 0 onto the stack
#  &#8594; 0L 
lconst_0 = MakeInstruction(0x09)

# push the long 1 onto the stack
#  &#8594; 1L 
lconst_1 = MakeInstruction(0x0a)

# push a constant ''#index'' from a constant pool (String, int or float)
#  onto the stack
#  &#8594; value 
ldc = MakeInstruction(0x12,'B')

# push a constant ''#index'' from a constant pool (String, int or float)
#  onto the stack (wide ''index'' is constructed as ''indexbyte1 &lt;&lt
# ; 8 + indexbyte2'')
#  &#8594; value 
ldc_w = MakeInstruction(0x13,'H')

# push a constant ''#index'' from a constant pool (double or long) onto 
# the stack (wide ''index'' is constructed as ''indexbyte1 &lt;&lt; 8 + 
# indexbyte2'')
#  &#8594; value 
ldc2_w = MakeInstruction(0x14,'H')

# divide two longs
#  value1, value2 &#8594; result 
ldiv = MakeInstruction(0x6d)

# load a long value from a local variable ''#index''
#  &#8594; value 
lload = MakeInstruction(0x16,'B')

# load a long value from a local variable 0
#  &#8594; value 
lload_0 = MakeInstruction(0x1e)

# load a long value from a local variable 1
#  &#8594; value 
lload_1 = MakeInstruction(0x1f)

# load a long value from a local variable 2
#  &#8594; value 
lload_2 = MakeInstruction(0x20)

# load a long value from a local variable 3
#  &#8594; value 
lload_3 = MakeInstruction(0x21)

# multiply two longs
#  value1, value2 &#8594; result 
lmul = MakeInstruction(0x69)

# negate a long
#  value &#8594; result 
lneg = MakeInstruction(0x75)

# a target address is looked up from a table using a key and execution c
# ontinues from the instruction at that address
#  key &#8594; 
lookupswitch = MakeInstruction(0xab,'L')

# bitwise or of two longs
#  value1, value2 &#8594; result 
lor = MakeInstruction(0x81)

# remainder of division of two longs
#  value1, value2 &#8594; result 
lrem = MakeInstruction(0x71)

# return a long value
#  value &#8594; [empty] 
lreturn = MakeInstruction(0xad)

# bitwise shift left of a long ''value1'' by ''value2'' positions
#  value1, value2 &#8594; result 
lshl = MakeInstruction(0x79)

# bitwise shift right of a long ''value1'' by ''value2'' positions
#  value1, value2 &#8594; result 
lshr = MakeInstruction(0x7b)

# store a long ''value'' in a local variable ''#index''
#  value &#8594; 
lstore = MakeInstruction(0x37,'B')

# store a long ''value'' in a local variable 0
#  value &#8594; 
lstore_0 = MakeInstruction(0x3f)

# store a long ''value'' in a local variable 1
#  value &#8594; 
lstore_1 = MakeInstruction(0x40)

# store a long ''value'' in a local variable 2
#  value &#8594; 
lstore_2 = MakeInstruction(0x41)

# store a long ''value'' in a local variable 3
#  value &#8594; 
lstore_3 = MakeInstruction(0x42)

# subtract two longs
#  value1, value2 &#8594; result 
lsub = MakeInstruction(0x65)

# bitwise shift right of a long ''value1'' by ''value2'' positions, unsi
# gned
#  value1, value2 &#8594; result 
lushr = MakeInstruction(0x7d)

# bitwise exclusive or of two longs
#  value1, value2 &#8594; result 
lxor = MakeInstruction(0x83)

# enter monitor for object ("grab the lock" - start of synchronized() se
# ction)
#  objectref &#8594; 
monitorenter = MakeInstruction(0xc2)

# exit monitor for object ("release the lock" - end of synchronized() se
# ction)
#  objectref &#8594; 
monitorexit = MakeInstruction(0xc3)

# create a new array of ''dimensions'' dimensions with elements of type 
# identified by class reference in constant pool ''index'' (''indexbyte1
#  &lt;&lt; 8 + indexbyte2''); the sizes of each dimension is identified
#  by ''count1'', [''count2'', etc.]
#  count1, [count2,...] &#8594; arrayref 
multianewarray = MakeInstruction(0xc5)

# create new object of type identified by class reference in constant po
# ol ''index'' (''indexbyte1 &lt;&lt; 8 + indexbyte2'')
#  &#8594; objectref 
new = MakeInstruction(0xbb,'H')

# create new array with ''count'' elements of primitive type identified 
# by ''atype''
#  count &#8594; arrayref 
newarray = MakeInstruction(0xbc,'B')

# perform no operation
#  [No change] 
nop = MakeInstruction(0x00)

# discard the top value on the stack
#  value &#8594; 
pop = MakeInstruction(0x57)

# discard the top two values on the stack (or one value, if it is a doub
# le or long)
#  {value2, value1} &#8594; 
pop2 = MakeInstruction(0x58)

# set field to ''value'' in an object ''objectref'', where the field is 
# identified by a field reference ''index'' in constant pool (''indexbyt
# e1 &lt;&lt; 8 + indexbyte2'')
#  objectref, value &#8594; 
putfield = MakeInstruction(0xb5,'H')

# set static field to ''value'' in a class, where the field is identifie
# d by a field reference ''index'' in constant pool (''indexbyte1 &lt;&l
# t; 8 + indexbyte2'')
#  value &#8594; 
putstatic = MakeInstruction(0xb3,'H')

# continue execution from address taken from a local variable ''#index''
#  (the asymmetry with jsr is intentional)
#  [No change] 
ret = MakeInstruction(0xa9,'B')

# return void from method
#  &#8594; [empty] 
vreturn = MakeInstruction(0xb1)

# load short from array
#  arrayref, index &#8594; value 
saload = MakeInstruction(0x35)

# store short to array
#  arrayref, index, value &#8594; 
sastore = MakeInstruction(0x56)

# push a short onto the stack
#  &#8594; value 
sipush = MakeInstruction(0x11,'H')

# swaps two top words on the stack (note that value1 and value2 must not
#  be double or long)
#  value2, value1 &#8594; value1, value2 
swap = MakeInstruction(0x5f)

# continue execution from an address in the table at offset ''index''
#  index &#8594; 
tableswitch = MakeInstruction(0xaa,'L')

# execute ''opcode'', where ''opcode'' is either iload, fload, aload, ll
# oad, dload, istore, fstore, astore, lstore, dstore, or ret, but assume
#  the ''index'' is 16 bit; or execute iinc, where the ''index'' is 16 b
# its and the constant to increment by is a signed 16 bit short
#  [same as for corresponding instructions] 
wide = MakeInstruction(0xc4)
