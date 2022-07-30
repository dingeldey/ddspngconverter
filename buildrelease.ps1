conda activate bmsbriefing

# This allows installer to pack required DDLs like _ssl
pyinstaller.exe --clean -F -y --paths C:\miniconda\pkgs\openssl-1.1.1l-h8ffe710_0\Library\bin dds2png.py 
pyinstaller.exe --clean -F -y --paths C:\miniconda\pkgs\openssl-1.1.1l-h8ffe710_0\Library\bin png2dds.py 

rm -r .\build

