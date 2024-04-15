# workerd RTTI in Python

This is a look into how to read and use the generated RTTI info in workerd.

Files:

- *.capnp.bin -- copied from bazel-out/(target)/bin/src/workerd/tools
- print_rtti.py -- a script that prints the textual format of a .capnp.bin file containing a StructureGroup
- rtti.capnp -- copied from src/workerd/jsg/rtti.capnp
- *.capnp.bin.txt -- generated text-format capnp files for examination