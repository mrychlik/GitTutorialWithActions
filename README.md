# Git Tutorial With Actions

NOTE: This is a Git repository for demo purpose only!


## GitHub and academic projects

GitHub has a general academic program, which allows promoting your
account to PRO. This eliminates a 100MB limit on repository size and adds some other useful features.


## Integration of a GitHub project with your desktop environment

* I create most content (code, TeX, etc. with Emacs). If you are using some kind of IDE, check if it integrates with Git.
* Emacs has Git integration, so most of the common operations on Git repository are a single keystroke operations.
	
* If you do not want to retype credentials every , do this after checkout:

	git config credential.helper 'cache --timeout=3000000'

This is very important when using integration with your development software (Emacs, Vim, etc.)
	
	
#  Python and 'pytest'

If you run 'pytest' or 'python -m pytest' in this folder, functions
named test_* in the file test_me.py will be run.


#  Automation of testing

Unit testing is extremely important for reproducibility of
results. Automation of unit testing is the best solution to natural
avoidance of testing, because it is time consuming and an annoyance.

You use ***GitHub*** feature called 'Actions'. Things to remember:

* Testing is performed by a virtual machine running an OS, e.g. Ubuntu.
* One can install software into the OS, to run any kind of code.
* Actions are normally triggered by any 'push' to the GitHub repository.
* Actions are described in files residing in a folder named .github and are best
  written in a language named YAML (Yet Another Markup Language)



	
