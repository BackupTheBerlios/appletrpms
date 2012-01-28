#! /bin/sh
# last modified: 2000-08-26
#
# A small script to launch a browser by clicking an URL-button.

opera=/usr/bin/opera
firefox=/usr/bin/firefox
lynx=/usr/bin/lynx
links=/usr/bin/links

urxvt=/usr/bin/urxvt
rxvt=/usr/bin/rxvt
eterm=/usr/bin/eterm
aterm=/usr/bin/aterm
xterm=/usr/bin/xterm
gnometerminal=/usr/bin/gnome-terminal

if [ "$1" != "" ]; then
  if [ -x $opera ]; then
    $opera -remote "openURL($1,new-window)" || $opera "$1" &
  elif [ -x $firefox ]; then
    $firefox -remote "openURL($1,new-window)" || $firefox "$1" &
  elif [ -x $lynx ]; then
    if [ -x $urxvt ]; then	
      $urxvt -title "Lynx Web Browser" -tr -fg yellow -bg black -e lynx "$1" &
    elif [ -x $rxvt ]; then
      $rxvt -title "Lynx Web Browser" -tr -fg yellow -bg black -e lynx "$1" &
    elif [ -x $eterm ]; then
      $eterm -title "Lynx Web Browser" -tr -tint blue -fg yellow -bg black -e lynx "$1" &
    elif [ -x $aterm ]; then
      $aterm -title "Lynx Web Browser" -tr -tint blue -fg yellow -bg black -e lynx "$1" &
    elif [ -x $xterm ]; then
      $xterm -T "Lynx Web Browser" -fg yellow -bg blue -e lynx "$1" &
    elif [ -x $gnometerminal ]; then
      $gnometerminal -t "Lynx Web Browser" -fg yellow -bg blue -e lynx "$1" &
    fi
  elif [ -x $links ]; then
    if [ -x $urxvt ]; then	
      $urxvt -title "Links Web Browser" -tr -fg yellow -bg black -e links "$1" &
    elif [ -x $rxvt ]; then
      $rxvt -title "Links Web Browser" -tr -fg yellow -bg black -e links "$1" &
    elif [ -x $eterm ]; then
      $eterm -title "Links Web Browser" -tr -tint blue -fg yellow -bg black -e links "$1" &
    elif [ -x $aterm ]; then
      $aterm -title "Links Web Browser" -tr -tint blue -fg yellow -bg black -e links "$1" &
    elif [ -x $xterm ]; then
      $xterm -T "Links Web Browser" -fg yellow -bg blue -e links "$1" &
    elif [ -x $gnometerminal ]; then
      $gnometerminal -t "Links Web Browser" -fg yellow -bg blue -e links "$1" &
    fi
  else
    echo "browser.sh: Failed to start browser!"
  fi
fi
