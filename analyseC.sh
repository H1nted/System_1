clear

for mot in "$@"
do
    for f in *
    do
        if [ -f "$f" ]
        then
            var=$(grep -c "bonjour" $f)
            #var2=$(grep -c "hello" $f)
            if (( var > 0 )) 
            then
            echo $mot a été trouvé $var fois dans $f
            fi
        fi
    done
done
