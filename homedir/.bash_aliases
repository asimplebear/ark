#
[ -z "$PS1" ] && return

#\j is # jobs currently managed by this shell
#\W is current directory
PS1='\j:\W>'

alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias p="python2"
alias p3="python3"

alias pwm="~/Scripts/pwm.sh"
mpw() {
	echo $1 | sha256sum | cut -c1-16;
}



mcd() {
	mkdir -p $1;
	cd $1;
}


alias gl="git log --all --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)' --abbrev-commit"

alias tre="tree -I 'network|fall2020|Downloads'"

#command line "script" starts recording terminal
#session and saves to "typescript"
#this cleans it up and writes to $1
cleanscript() {
sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[mGK]//g" typescript | tr -dc '[[:print:]]\n' > $1

}

#json contents of $1 filename
#prettified and written to $2 filename
pjson() {
cat $1 | python3 -m json.tool > $2
}


alias konk="conky -b &"
alias killkonk="killall conky"


toclip() {
/home/tbear/Scripts/toclip.py $1
}
fromclip() {
/home/tbear/Scripts/fromclip.py $1
}

treee() {
  tree -I __pycache__;
}

#export PATH="/home/tbear/.sass/dart-sass:$PATH"
export PATH="$PWD/.dart-sass:$PATH"

allkeys() {
  cp /home/tbear/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml xfce4-keyboard-shortcuts.xml;
  /home/tbear/Scripts/keyboard/keyboard.py;
}

keys() {
  allkeys | grep $1;
}
