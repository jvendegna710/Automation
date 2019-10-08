start /W php N:\EDI1\JudgmentEntry\NewYork\Judgment_Record_Entry.php
echo NY Record Creation Complete  
start /W py N:\EDI1\JudgmentEntry\NewYork\JudgmentEntryAuto.py
echo Waiting for NY to complete entry. It takes a while sometimes.

start /W py N:\EDI1\JudgmentEntry\NewYork\sleep.py
echo NY Judgment Entered

start /W php N:\EDI1\JudgmentEntry\NewJersey\NEW_JERSEYJudgment_Record_Entry.php
echo NJ Record Creation Complete   
start /W py N:\EDI1\JudgmentEntry\NewJersey\NEW_JERSEY_JudgmentEntryAuto.py
echo NJ Judgment Entered 