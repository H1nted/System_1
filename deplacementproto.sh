clear

for extension in "$@"
do
    for fichier in *
    do 
        var=$(echo $fichier | cut -d . -f2)
        echo $var
        # if [ var = $extension ]
        # then 
        #     echo very nice they exist!
        # else
        #     echo not nice sad..
        # fi
    done
done