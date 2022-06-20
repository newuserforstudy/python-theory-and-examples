#!/bin/bash

PS3="Please select your system menu:"

select i in "CentOS" "RedHat" "Ubuntu"
do
  case $i in
  CentOS)
    echo "your select system is CentOS"
    break
    ;;

  RedHat)
    echo "your select system is RedHat"
    break
    ;;
  Ubuntu)
    echo "your select system is Ubuntu"
    break
    ;;
  *)
    echo "Usage is { $0 + 1 || 2 || 3 ||...}"
    break
  esac
done
