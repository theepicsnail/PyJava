import struct
import constants
import ConstantPool

def debug_print(*a):
    import traceback
    print len(traceback.extract_stack())*" ", a

def list_dump(lst, constant_pool, use_long = False):
    packing = ">H"
    if use_long:
        packing = ">L"
    data = "".join([item.dump(constant_pool) for item in lst])
    return struct.pack(packing, len(data)) + data
class Utf8:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return "Utf8({})".format(self.data)
    def dump(self, constant_pool):
        return struct.pack(">BH", 1, len(self.data)) + self.data
        
class ClassReference:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "ClassReference({})".format(self.name)
    def dump(self, constant_pool):
        assert isinstance(self.name, Utf8)
        return struct.pack(">BH", 7, constant_pool.get_id(self.name))        


class ClassFile:
    def __init__(self):
        self.magic = 0xCAFEBABE
        self.version = (0, 0) #major, minor
        self.access_flags = 0
        self.this_class = None # ClassRef
        self.super_class = None # ClassRef
        self.interfaces = []
        self.fields = []
        self.methods = []
        self.attributes = []

    def dump(self, constant_pool):
        #header   
        #table of constants
        #classdef 
        #interfaces
        #fields
        #methods
        #attributes 
        header = struct.pack(">LHH", 
            self.magic, 
            self.version[1], 
            self.version[0])
       
    
        assert isinstance(self.this_class, ClassReference)
        assert isinstance(self.super_class, ClassReference)
        classdef = struct.pack(">HHH", 
            self.access_flags,
            constant_pool.get_id(self.this_class),
            constant_pool.get_id(self.super_class))
        print "This:", self.this_class, constant_pool.get_id(self.this_class)
        interface_data = struct.pack(">H", len(self.interfaces))+\
            "".join([item.dump(constant_pool) for item in self.interfaces])

        field_data = struct.pack(">H", len(self.fields))+\
            "".join([item.dump(constant_pool) for item in self.fields])

        method_data = struct.pack(">H", len(self.methods))+\
            "".join([item.dump(constant_pool) for item in self.methods])

        attribute_data = struct.pack(">H", len(self.attributes))+\
            "".join([item.dump(constant_pool) for item in self.attributes])
        
        #print "header", map(ord, header)
        #print "classdef", map(ord, classdef)
        #print "interface_data", map(ord, interface_data)
        #print "field_data", map(ord, field_data)
        #print "method_data"
        #print " ".join(map(lambda d: "%3i"%ord(d), method_data))
        #print "attribute_data", map(ord, attribute_data)

        return header +\
            constant_pool.dump() +\
            classdef +\
            interface_data +\
            field_data +\
            method_data +\
            attribute_data

Spec = """
 ClassFile {
        u4 magic;
        u2 minor_version;
        u2 major_version;
        u2 constant_pool_count;
        cp_info constant_pool[constant_pool_count-1];
        u2 access_flags;
        u2 this_class;
        u2 super_class;
        u2 interfaces_count;
*        u2 interfaces[interfaces_count];
        u2 fields_count;
        field_info fields[fields_count];
        u2 methods_count;
        method_info methods[methods_count];
        u2 attributes_count;
        attribute_info attributes[attributes_count];
    }
"""

class FieldReference:
    def __init__(self):
        self.classref = None
        self.name_and_desc = None
    def __str__(self):
        return "FieldReference({}, {})".format(self.classref, self.name_and_desc)

    def dump(self, constant_pool):
        assert isinstance(self.classref, ClassReference)
        assert isinstance(self.name_and_desc, NameAndDescription)
        return struct.pack(">BHH",
            9,
            constant_pool.get_id(self.classref), 
            constant_pool.get_id(self.name_and_desc))
class StringReference:
    def __init__(self, string):
        self.string = string
    def dump(self, c):
        return struct.pack(">BH",
            8,
            c.get_id(self.string))
class MethodReference:
    def __init__(self):
        self.classref = None
        self.name_and_desc = None
    def __str__(self):
        return "MethodReference({}, {})".format(self.classref, self.name_and_desc)

    def dump(self, constant_pool):
        assert isinstance(self.classref, ClassReference)
        assert isinstance(self.name_and_desc, NameAndDescription)
        return struct.pack(">BHH",
            10,
            constant_pool.get_id(self.classref), 
            constant_pool.get_id(self.name_and_desc))

class NameAndDescription:
    def __init__(self):
        self.name = None
        self.description = None
    
    def __str__(self):
        return "NameAndDescription({}, {})".format(self.name, self.description)

    def dump(self, constant_pool):
        assert isinstance(self.name, Utf8)
        assert isinstance(self.description, Utf8)
        return struct.pack(">BHH", 12,
            constant_pool.get_id(self.name),
            constant_pool.get_id(self.description))

class MethodInfo:
    def __init__(self):
        self.access_flags = 0
        self.name = None
        self.description = None
        self.attributes = []
    def __str__(self):
        return "MethodInfo({}, {}, {}, [{}])".format(
           bin(self.access_flags)[2:],
           self.name,
           self.description,
           ",".join(map(str, self.attributes))
        )
    def dump(self, constant_pool):
        attr_data = "".join([
                attr.dump(constant_pool) 
                for attr in self.attributes])
        return struct.pack(">HHHH",
            self.access_flags,
            constant_pool.get_id(self.name),
            constant_pool.get_id(self.description),
            len(self.attributes))+ attr_data\
        

class Attribute:
    def __init__(self):
        self.name = None

    def dump(self, constant_pool):
        data = self.attr_dump(constant_pool)
        return struct.pack(">HL",
            constant_pool.get_id(self.name),
            len(data))+ data
            
    def attr_dump(self, constant_pool):
        assert False # Not implemented.

class CodeAttribute(Attribute):
    def __init__(self):
        Attribute.__init__(self)
        self.max_stack = 0
        self.max_locals = 0
        self.code = []
        self.exception_table = []
        self.attributes = []

    def attr_dump(self, constant_pool):
        print "code stack ",self.max_stack
        print "code locals",self.max_locals
        print "code code",self.code
        print "code exceptions",self.exception_table
        print "code attributes",self.attributes
        attr_data = "".join([
            attr.dump(constant_pool)
            for attr in self.attributes])

        return struct.pack(">HH",
            self.max_stack,
            self.max_locals)+\
            list_dump(self.code, constant_pool, True)+\
            list_dump(self.exception_table, constant_pool)+\
            struct.pack(">H", len(self.attributes))+attr_data 

class SourceFileAttribute():
    def __init__(self, source):
        #Attribute.__init__(self)
        self.source = source
        self.name = Utf8("SourceFile")
    def dump(self, c):
        return struct.pack(">HLH", c.get_id(self.name), 2, c.get_id(self.source))

class LineNumberTable:
    def __init__(self, *table):
        self.table = table

    def dump(self, c):
        table_idx = c.get_id(Utf8("LineNumberTable"))
        lntout = struct.pack(">H", len(self.table)) + "".join([
            struct.pack(">HH", *entry)
            for entry in self.table
        ])
        lntout = struct.pack(">HL", table_idx, len(lntout)) + lntout
        return lntout

class GetStatic:
    def __init__(self, idx):
        self.idx = idx
    def dump(self, c):
        return struct.pack(">BH", 0xb2, self.idx)

class LoadArg0:
    def dump(self, c):
        return struct.pack("B", 0x2a)

class InvokeSpecial:
    def __init__(self, idx):
        self.idx = idx
    def dump(self, c):
        return struct.pack(">BH", 0xb7, self.idx)

class Return:
    def dump(self, c):
        return struct.pack("B", 0xb1)
class LoadConstant:
    def __init__(self, constant):
        self.constant = constant

    def dump(self, c):
        return struct.pack(">BB", 0x12, self.constant)

class InvokeVirtual:
    def __init__(self, func):
        self.func = func
    def dump(self, c):
        return struct.pack(">BH", 0xb6, self.func)




#import pdb; pdb.set_trace()
constant_pool = ConstantPool.ConstantPool()

c = ClassFile()
c.version = constants.JAVA_6
c.access_flags = constants.PUBLIC | constants.SUPER
c.this_class = ClassReference(Utf8("TEST"))
c.super_class = ClassReference(Utf8("java/lang/Object"))

mref1 = MethodReference()
mref1.classref = ClassReference(Utf8("java/lang/Object"))
mref1.name_and_desc = NameAndDescription()
mref1.name_and_desc.name = Utf8("<init>")
mref1.name_and_desc.description = Utf8("()V") 

code1 = CodeAttribute()
code1.name = Utf8("Code") 
code1.max_stack = 1
code1.max_locals = 1
code1.code = [
    LoadArg0(),
    InvokeSpecial(constant_pool.get_id(mref1)),
    Return()
]
code1.attributes.append(
    LineNumberTable((0,1))
)
method1 = MethodInfo()
method1.access_flags = constants.PUBLIC
method1.name = Utf8("<init>")
method1.description = Utf8("()V")
method1.attributes.append(code1)
c.methods.append(method1)

fref1 = FieldReference()
fref1.classref = ClassReference(Utf8("java/lang/System"))
fref1.name_and_desc = NameAndDescription()
fref1.name_and_desc.name = Utf8("out")
fref1.name_and_desc.description = Utf8("Ljava/io/PrintStream;")

sref1 = StringReference(Utf8("Hello world"))

mref2 = MethodReference()
mref2.classref = ClassReference(Utf8("java/io/PrintStream"))
mref2.name_and_desc = NameAndDescription()
mref2.name_and_desc.name = Utf8("println")
mref2.name_and_desc.description = Utf8("(Ljava/lang/String;)V")

code2 = CodeAttribute()
code2.name = Utf8("Code")
code2.max_stack = 20
code2.max_locals = 1
code2.code = [
    GetStatic(constant_pool.get_id(fref1)),
    LoadConstant(constant_pool.get_id(sref1)),
    InvokeVirtual(constant_pool.get_id(mref2)),
    GetStatic(constant_pool.get_id(fref1)),
    LoadConstant(constant_pool.get_id(sref1)),
    InvokeVirtual(constant_pool.get_id(mref2)),
    Return()
]
code2.attributes.append(
    LineNumberTable((0,3), (8, 4))
)
method2 = MethodInfo()
method2.access_flags = constants.PUBLIC | constants.STATIC
method2.name = Utf8("main")
method2.description = Utf8("([Ljava/lang/String;)V")
method2.attributes.append(code2)
c.methods.append(method2)
c.attributes.append(SourceFileAttribute(Utf8("TEST.java")))

data = c.dump(constant_pool)
constant_pool.debug_dump()
file("TEST.class","w").write(data)

