data = file("wiki").readlines()
data = data[::2]
for i in filter(lambda x:not x.startswith("|-"), data):
    _, name, _, _, op, _, args, _, diff, _, doc =  i.split("|")
    op = "0x"+op.strip()
    doc = doc.strip()
    diff = diff.replace("\xe2\x86\x92", "->")
    args = args.strip()
    name = name.strip()
    packing = ""
    if args.startswith("1"):
        packing = "B"
    elif args.startswith("2"):
        packing = "H"
    elif args.startswith("4"):
        packing = "L"
    if packing:
        packing = ",'" + packing +"'"
    
    doc = "\n".join(["# " + doc[i:i+70] for i in xrange(0,len(doc),70)])
    doc += "\n# " + diff
    print "\n{}\n{} = MakeInstruction({}{})".format(doc, name, op, packing)
