fname="E:\chengpeng.github.io\Hack\hello.bmp"

pfile=open(fname,"r+b")
buff=pfile.read()
buff.replace(b'\x2A\x2F',b'\x00\x00')
pfile.close()

pfile = open (fname, "w+b")
pfile.write (buff)
pfile.seek(2,0)
pfile.write (b'\x2F\x2A')
pfile.close ()

pfile=open (fname, "a+b")
pfile.write(b'\xFF\x2A\x2F\x3D\x31\x3B')
pfile.write (open('E:\chengpeng.github.io\Hack\hello.js','rb').read())
pfile. close()