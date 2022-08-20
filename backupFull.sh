#!/bin/bash

data=$(date +'%Y_%m_%d_%H_%M_%S')
arquivo=backup_full_$1_$data
tar -czvf $arquivo.tar.gz $1
gpg -c $arquivo.tar.gz
