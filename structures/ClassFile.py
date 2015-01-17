"""
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
        u2 interfaces[interfaces_count];
        u2 fields_count;
        field_info fields[fields_count];
        u2 methods_count;
        method_info methods[methods_count];
        u2 attributes_count;
        attribute_info attributes[attributes_count];
    }

"""
import struct
from ConstantPool import ConstantPool

class ClassFile:
    magic = 0xCAFEBABE
    version = None     # 
    access_flags = None# bit vector
    this_class = None  # Class reference
    super_class = None # Class reference
    interfaces = []    # List of Interface objects
    fields = []        # List of field objects
    methods = []       # List of method objects
    attributes = []    # List of attribute objects

    def dump(self):
        constant_pool = ConstantPool()
        header_data = struct.pack(">LHH", self.magic, 
                    self.version[1], self.version[0])

        tail_data = struct.pack(">HHH", 
                                self.access_flags, 
                                constant_pool.get(self.this_class), 
                                constant_pool.get(self.super_class))
         

        interface_data = struct.pack(">H", len(self.interfaces))
        interface_data += "".join([
            intf.dump(constant_pool)
            for intf in self.interfaces
        ])
        
        field_data = struct.pack(">H", len(self.fields))
        field_data += "".join([
            f.dump(constant_pool)
            for f in self.fields
        ])

        method_data = struct.pack(">H", len(self.methods))
        method_data += "".join([
            m.dump(constant_pool)
            for m in self.methods
        ])

        attribute_data = struct.pack(">H", len(self.attributes))
        attribute_data += "".join([
            intf.dump(constant_pool)
            for intf in self.attributes
        ])


        return header_data +\
            constant_pool.dump() +\
            tail_data +\
            interface_data +\
            field_data +\
            method_data +\
            attribute_data
