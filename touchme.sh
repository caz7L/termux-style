#!/usr/bin/bash
printf "Check python"
sleep 0.3
printf "."
sleep 0.3
printf "."
sleep 0.3
printf "."
sleep 0.5
if [ -f $PREFIX/bin/python ]; then
	echo "OK"
else
	echo -e "NOPE\nInstalling python"
	pkg install python -y
fi
clear
echo "Moving"
if [ -r $HOME/.termux ]; then
	echo -n
else
	mkdir $HOME/.termux
fi
mv * $HOME/.termux
echo -e "cd $HOME/.termux\npython main.py">termux-style
chmod +x termux-style
mv termux-style $PREFIX/bin
clear
echo -e "Done!\ntype \"termux-style\" to run it"
