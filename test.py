from structures.ClassFile import ClassFile
from structures.ConstantPool import ConstantPool
from structures.Constants import *
from structures.InfoClasses import *
from structures.Instructions import *

def public_static_void_main(code):
    return MethodInfo(PUBLIC | STATIC,
        Utf8Info("main"),
        #array of instances of class string
        Utf8Info(DESCRIPTOR(ARRAY_OF(INSTANCE_OF("java/lang/String")))),
        [code])

def make_basic_class(class_name, super_name ="java/lang/Object"):
    """
    Create a public class, named {class_name} with a 0 argument
    constructor.
    """
    # setup the class
    c = ClassFile()
    c.version = JAVA_6
    c.access_flags = PUBLIC | SUPER
    c.this_class = ClassInfo(Utf8Info(class_name))
    c.super_class = ClassInfo(Utf8Info(super_name))

    # setup the super constructor reference
    s_constructor_ref = MethodReferenceInfo(
        ClassInfo(Utf8Info(super_name)),
        NameAndTypeInfo(Utf8Info("<init>"), Utf8Info("()V")))

    # setup the constructor code
    constructor_code = CodeAttribute(
        2, #stack
        1, #locals
        [ aload_0() #code
        , invokespecial(s_constructor_ref)
        , vreturn() ],
        [], #exceptions
        [LineNumberTableAttribute([LineNumberTableEntry(0,1)])])

    # setup the constructor method
    constructor = MethodInfo(PUBLIC, Utf8Info("<init>"), Utf8Info("()V"),
                    [constructor_code])
    c.methods.append(constructor)
    c.attributes.append(SourceFileAttribute(Utf8Info(class_name + ".java")))
    return c

#Set up references we'll need in the code

#System.out (is a PrintStream)
system_out = FieldReferenceInfo(
    ClassInfo(Utf8Info("java/lang/System")),
    NameAndTypeInfo(Utf8Info("out"),
    Utf8Info(INSTANCE_OF("java/io/PrintStream"))))

#PrintStream.println (taking a string)
printstream_println = MethodReferenceInfo(
    ClassInfo(Utf8Info("java/io/PrintStream")),
    NameAndTypeInfo(Utf8Info("println"),
    Utf8Info(DESCRIPTOR(INSTANCE_OF("java/lang/String")))))

code = CodeAttribute(4, 1, [
    getstatic(system_out), #[ system_out
    ldc(StringInfo(Utf8Info("Hello world"))),
    invokevirtual(printstream_println),
    vreturn()
],[],[LineNumberTableAttribute([
    LineNumberTableEntry(0,3),
])])

my_class = make_basic_class("Test")
my_class.methods.append(public_static_void_main(code))

file("Test.class","w").write(my_class.dump())

