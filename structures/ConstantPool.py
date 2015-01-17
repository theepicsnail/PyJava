import struct
class ConstantPool:
    def __init__(self):
        self.pool = {}
        self.next_id = 1
        self.pooldata = ""

    def get(self, key):
        dump = key.dump(self)
        if dump not in self.pool:
            self.pool[dump] = (self.next_id, key)
            self.next_id += 1
            self.pooldata += dump  + ""
        key_id = self.pool[dump][0]

        #print "Id:", key_id, "for", str(key), "=", map(ord, dump)
        return key_id

    def debug_dump(self):
        dumps =  self.pool.keys()
        for k in sorted(dumps, key=self.pool.get):
            print map(str,self.pool[k])

    def dump(self):
        print len(self.pooldata)
        #self.debug_dump ()
        #print "Actual len:", len(self.pooldata)
        return struct.pack(">H", self.next_id) + self.pooldata
