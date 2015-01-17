import struct

import sys

with file(sys.argv[1] + ".class", "rb") as FILE:
    def read(fmt, as_hex=True):
        size = struct.calcsize(fmt)
        data = FILE.read(size)
        return struct.unpack(fmt, data)
    table = {}
    def read_table(n):
        table = {}
        idx = 0
        while idx < n-1:
            idx += 1
            label = read(">B")[0]
            if label == 1:
                data_len = read(">H")[0]
                data =FILE.read(data_len)
            elif label == 7:
                data = read(">H")[0]
                data = "ClassReference({r%s})" % data
            elif label == 8:
                data = read(">H")[0]
                data = "StringReference({r%s})" % data
            elif label == 9:
                data = read(">HH")
                data = "Field({r%s},{r%s})" % data
            elif label == 10:
                data = read(">HH")
                data = "Method({r%s},{r%s})" % data
            elif label == 12:
                data = read(">HH")
                data = "NAT({r%s},{r%s})" % data
            else:
                data = "Unknown label " + str(label)
                idx -= 1
                #assert(False)
            table["r%s" % idx]=data

        out = {}
        for idx in xrange(1, n):
            key = "r%s" % idx
            while "{" in table[key]:
                table[key] = table[key].format(**table)
            out[(idx,)] = table[key]
            print "%2s" % idx, table[key]
        return out

    print "Magic", map(hex, read(">L"))
    print "Version", map(hex, read(">HH"))
    t = read(">H")[0]
    print "Table count", t
    table = read_table(t)
    print "Access", read(">H")
    print "This ", table[read(">H")] # class ref -> utf
    print "Super", table[read(">H")] # class ref -> utf

    print "Interfaces:", read(">H")
    print "Fields:", read(">H")
    print "Methods:", read(">H")
    for i in xrange(2):
        print "Method",i
        print "  Access flags", read(">H")
        print "  Name        ", table[read(">H")]
        print "  Descriptor  ", table[read(">H")]
        a = read(">H")[0]
        print "  Attributes: ", a
        for j in xrange(a):
            print "  Attribute",j
            print "    type ", table[read(">H")]
            print "    attr_len ", read(">L")
            print "      stack  ", read(">H")
            print "      locals ", read(">H")
            code_len = read(">L")[0]
            print "      codelen", code_len
            for k in xrange(code_len):
                print "        ", hex(read(">B")[0])
            print "      excepts", read(">H")
            code_attrs = read(">H")[0]
            print "      attrs", code_attrs
            for k in xrange(code_attrs):
                print "      Attr", k
                print "        type ", table[read(">H")]
                print "        len  ", read(">L")
                count = read(">H") [0]
                print "        count", count
                for l in xrange(count):
                    print "          ", read(">HH")
    print "Attributes:", read(">H")
    print "  Type ", table[read(">H")]
    print "  Len  ", read(">L")
    print "  Data ", read(">H")
