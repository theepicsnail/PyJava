# http://docs.oracle.com/javase/specs/jvms/se7/html/jvms-2.html#jvms-2.1
# http://docs.oracle.com/javase/specs/jvms/se5.0/html/ClassFile.doc.html

#Data types
BYTE   = 'B'
CHAR   = 'C'
DOUBLE = 'D'
FLOAT  = 'F'
INT    = 'I'
LONG   = 'J'
SHORT  = 'S'
VOID   = 'V'
BOOLEAN= 'Z'
ARRAY_OF = lambda class_name: '[' + class_name
INSTANCE_OF = lambda class_name: class_name.join("L;")

DESCRIPTOR = lambda args="", ret=VOID: "(" + args + ")" + ret
#Access flags
PUBLIC    = 0x0001 # Declared public; may be accessed from outside its package.
PRIVATE   = 0x0002 # Declared private; usable only within the defining class.
PROTECTED = 0x0004 # Declared protected; may be accessed within subclasses.
STATIC    = 0x0008 # Declared static.
FINAL     = 0x0010 # Declared final; no further assignment after initialization.
SUPER     = 0x0020 # Treat superclass methods specially when invoked by the invokespecial instruction.
VOLATILE  = 0x0040 # Declared volatile; cannot be cached.
TRANSIENT = 0x0080 # Declared transient; not written or read by a persistent object manager.
NATIVE    = 0x0100 # Declared native; implemented in a language other than Java.
INTERFACE = 0x0200 # Is an interface, not a class.
ABSTRACT  = 0x0400 # Declared abstract; may not be instantiated.

#Versions (major, minor)
JAVA_7 = (0x33, 0) # J2SE 7
JAVA_6 = (0x32, 0) # J2SE 6
JAVA_5 = (0x31, 0) # J2SE 5
JAVA_4 = (0x30, 0) # JDK 1.4
JAVA_3 = (0x2F, 0) # JDK 1.3
JAVA_2 = (0x2E, 0) # JDK 1.2
JAVA_1 = (0x2D, 0) # JDK 1.1


