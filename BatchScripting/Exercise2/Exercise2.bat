@echo off
setlocal EnableDelayedExpansion
if not exist TextFiles (
  mkdir TextFiles
)
if not exist SourceFiles (
  mkdir SourceFiles
)
if not exist HeaderFiles (
  mkdir HeaderFiles
)

for /f "tokens=1-4" %%a in (input.txt) do (
 echo %%a
if not exist %%a (
  mkdir %%a
 )
 
echo %%b
echo %%c
echo %%d
 
 
 cd %%a
if exist %%b (
  SET /p content=<%%b
	set /a content += 1
	
	echo !content!>%%b
 ) else (
 attrib -r %%b
 ECHO 0 >%%b
 )
if exist %%c (
  SET /p content=<%%c
	set /a content += 1
	echo !content!>%%c

 ) else (
 attrib -r %%c
 ECHO 0 >%%c
 )
if exist %%d (
  SET /p content=<%%d
	set /a content += 1
	echo !content!>%%d
 ) else (
 attrib -r %%d
 ECHO 0 >%%d
 )
 cd ..
  COPY /Y %%a\*.txt TextFiles>nul
 COPY /Y %%a\*.c SourceFiles>nul
 COPY /Y %%a\*.h HeaderFiles>nul
)

