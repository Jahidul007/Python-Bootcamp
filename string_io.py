import io
message = 'this is just normal string.'

f = io.StringIO(message)
f.read()
f.write(' second line written to file like object')
f.seek(0)
print(f.read())
