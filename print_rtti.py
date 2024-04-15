import capnp
import rtti_capnp
import sys

if len(sys.argv) != 2:
    print("usage: print_rtti.py <capnp.bin file>")

with open(sys.argv[1], 'rb') as f:
    api = rtti_capnp.StructureGroups.read(f)
    print(api)