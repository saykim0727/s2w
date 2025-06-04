@echo off
setlocal

set IDA_PATH="C:/Program Files/IDA Pro 8.4/idat64.exe"
set BINARY1=%~1
set BINARY2=%~2
for %%F in (%BINARY1%) do set NAME1=%%~nF
for %%F in (%BINARY2%) do set NAME2=%%~nF

%IDA_PATH% -A -S./script/bindiff.py -o%NAME1%.i64 %BINARY1%
%IDA_PATH% -A -S./script/bindiff.py -o%NAME2%.i64 %BINARY2%

bindiff .\%NAME1%.BinExport .\%NAME2%.BinExport

python3 script/compare.py %NAME1%.BinExport %NAME2%.BinExport

pause