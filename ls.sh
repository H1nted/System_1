clear

for variable in *
do
    if test -f $variable #
    then 
        ls -l $variable
    fi
done
