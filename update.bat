@echo off
git add .
set /p str=
git commit -m "%str%"
git push origin master
pause