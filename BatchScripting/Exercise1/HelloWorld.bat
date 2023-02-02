@ECHO OFF
SET text_value=%1
SET output_folder=%2
Set output_file=%3

if [%1]==[] GOTO INVALIDINPUT
if [%2]==[] GOTO INVALIDINPUT
if [%3]==[] GOTO INVALIDINPUT


IF EXIST %output_folder% (
MKDIR %output_folder%
)
CD %output_folder%
attrib -r %output_file%
ECHO %text_value%>%output_file%
attrib +r %output_file%
goto end
:INVALIDINPUT
echo "invalid input"
:END
