for %%A in (%3) do (
set fp=%%~dpA
set fn=%%~nA
set ext=%%~xA
)

molconvert mol %fn%%ext% -o %fp%eps\%fn%.mol
molconvert eps:H_hetero,mono,atsiz0.35,scale24,bondw0.09,bondl14.4,wireThickness0.021,boldbondw2 %fp%eps\%fn%.mol -o %fp%eps\%fn%.eps
REM molconvert png:H_hetero,mono,atsiz0.35,scale24,bondw0.09,bondl14.4,wireThickness0.021,boldbondw2,atomFont:SansSerif-ITALIC-10,#ffffff %fp%eps\%fn%.mol -o output.png
del %fp%eps\%fn%.mol
ren %fp%eps\%fn%.eps %fn%.eps.old
findstr /b /v fittopage %fp%eps\%fn%.eps.old > %fp%eps\%fn%.eps 
del %fp%eps\%fn%.eps.old
echo %fn%