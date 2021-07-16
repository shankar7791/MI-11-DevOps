1) SYSTEM VARIABLES
	Created and maintained by Linux bash shell itself. This type of variable (with the exception of auto_resume and histchars) is defined in CAPITAL LETTERS. You can configure aspects of the shell by modifying system variables such as PS1, PATH, LANG,HISTSIZE,and DISPLAY etc. 
	Commonly used system variables are BASH_VERSION , HOSTNAME ,CDPATH , HISTFILE , HISTSIZE , HOME.
	
	
2) USER DEFINED VARIABLES -
	Created and maintained by user. This type of variable defined may use any valid variable name, but it is good practice to avoid all uppercase names as many are used by the shell. 
	
	
	
3) SCRIPT FOR SYSTEM VARIABLE -
	#!/bin/bash
	# List contents of scratch
	echo “Executing script : \”$0\” with $# parameters”
	cd $RCAC_SCRATCH
	ls –l
