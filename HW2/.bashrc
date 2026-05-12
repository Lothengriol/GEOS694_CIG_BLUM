export CLICOLOR=1
alias ls='ls -G' # adapts ls to have colors
alias ll='ls -lG' # create a new command ll that outputs the long list with colors
# Set colorful prompt: cyan username, green hostname, blue directory
export PS1='\[\e[36m\]\u\[\e[0m\]@\[\e[32m\]\h\[\e[0m\]:\[\e[34m\]\w\[\e[0m\]\$ '

## this is sourced in the ~/.bash_profile file using: 
## if [ -f ~/.bashrc ]; then
## 	source ~/.bashrc
## fi
