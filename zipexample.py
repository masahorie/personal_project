import zipfile

new_zip = zipfile.ZipFile('test.zip', 'w')
new_zip.write('BS4_Test.py', compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()
