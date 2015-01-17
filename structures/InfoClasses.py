"""
"""
import struct

class Utf8Info:
    def __init__(self, data=None):
        self.data = data
    def dump(self, pool):
        return struct.pack(">BH", 1, len(self.data)) + self.data

#Class generator for the numeral primitives
def __PrimitiveClassGenerator(packing_char, tag_value):
    class Primitive:
        def __init__(self, val=None):
            self.val = val
        def dump(self, pool):
            return struct.pack(">B" + packing_char, tag_value, self.val)
    return Primitive
#No type 2 object
IntegerInfo = __PrimitiveClassGenerator("i", 3)
FloatInfo   = __PrimitiveClassGenerator("f", 4)
LongInfo    = __PrimitiveClassGenerator("l", 5)
DoubleInfo  = __PrimitiveClassGenerator("d", 6)

class ClassInfo:
    def __init__(self, name=None):
        self.name = name
    def dump(self, constant_pool):
        return struct.pack(">BH", 7, constant_pool.get(self.name))

class StringInfo:
    def __init__(self, utf8 = None):
        self.utf8 = utf8
    def dump(self, cp):
        return struct.pack(">BH", 8, cp.get(self.utf8))

def __RefClassGenerator(tag):
    class RefInfo:
        def __init__(self, clsInfo= None, natInfo=None):
            self.clsInfo = clsInfo
            self.natInfo = natInfo
        def dump(self, cp):
            return struct.pack(">BHH", tag, cp.get(self.clsInfo), cp.get(self.natInfo))
    return RefInfo
FieldReferenceInfo = __RefClassGenerator(9)
MethodReferenceInfo = __RefClassGenerator(10)
InterfaceMethodReferenceInfo = __RefClassGenerator(11)

class NameAndTypeInfo:
    def __init__(self, name = None, desc=None):
        self.name = name
        self.desc = desc
    def dump(self, cp):
        return struct.pack(">BHH", 12, cp.get(self.name), cp.get(self.desc))
#No type 13+ objects


class MethodInfo:
    def __init__(self, access_flags=None, name=None, desc=None, attributes = None):
        self.access_flags = access_flags #int
        self.name = name #utf8Info
        self.desc = desc #Utf8Info
        self.attributes = attributes if attributes is not None else [] #AttributeInfo

    def dump(self, cp):
        return struct.pack(">HHHH", 
            self.access_flags, 
            cp.get(self.name),
            cp.get(self.desc),
            len(self.attributes)) + "".join([
                attr.dump(cp)
                for attr in self.attributes
            ])

class AttributeInfo(object):
    def __init__(self, name = None):
        self.name = name

    def dump(self, cp):
        data = self.attr_dump(cp)
        return struct.pack(">HL", 
            cp.get(self.name),
            len(data)) + data

    def attr_dump(self, cp):
        raise Exception("Attribute did not override attr_dump")

class ConstantValueAttribute(AttributeInfo):
    def __init__(self, value):
        super(self.__class__, self).__init__(Utf8Info("ConstantValue"))
        self.value = value

    def attr_dump(self, cp):
        assert(type(self.value) in [LongInfo, FloatInfo, DoubleInfo, IntegerInfo, StringInfo])
        return struct.pack(">H", cp.get(self.value))

class CodeAttribute(AttributeInfo):
    def __init__(self, max_stack = 0, max_locals = 0, code = None, exceptions = None, attributes = None):
        super(self.__class__, self).__init__(Utf8Info("Code"))
        self.max_stack = max_stack
        self.max_locals = max_locals
        self.code = code if code is not None else []
        self.exceptions = exceptions if exceptions is not None else []
        self.attributes = attributes if attributes is not None else []

    def attr_dump(self, cp):
        code_data = "".join([instr.dump(cp) for instr in self.code])

        return struct.pack(">HHL", self.max_stack, self.max_locals, len(code_data)) +\
            code_data +\
            struct.pack(">H", len(self.exceptions)) +\
            "".join([exception.dump(cp) for exception in self.exceptions]) +\
            struct.pack(">H", len(self.attributes)) +\
            "".join([attrib.dump(cp) for attrib in self.attributes])

#Figure out exception/exceptionattributes
#InnerClassAttribute
#Synthetic
class SourceFileAttribute(AttributeInfo):
    def __init__(self, class_name=None):
        super(self.__class__, self).__init__(Utf8Info("SourceFile"))
        self.class_name = class_name

    def attr_dump(self, cp):
        return struct.pack(">H", cp.get(self.class_name))

class LineNumberTableAttribute(AttributeInfo):
    def __init__(self, table = None):
        super(self.__class__, self).__init__(Utf8Info("LineNumberTable"))
        self.table = table if table is not None else []
    def attr_dump(self, cp):
        return struct.pack(">H", len(self.table)) +\
            "".join([entry.dump(cp) for entry in self.table])

class LineNumberTableEntry:
    def __init__(self, start=None, line =None):
        self.start = start
        self.line = line
    def dump(self, cp):
        return struct.pack(">HH", self.start, self.line)

#LocalVariableTableAttribute
#Deprecated


