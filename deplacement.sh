clear


for extension in "$@"
do
    for fichier in *
    do
        if [ -f "$fichier" ]
        then
            echo il existe que des fichier
            if [ 'echo $fichier | cut -d . -f2' = $extension ]
            then
                echo l extension existe
                if [ ! -e "$*" ]
                then 
                    echo je creer le dossier $extension et je bouge les fichiers
                    mkdir $extension
                    mv $fichier $extension
                else
                    echo $extension existe donc je vais juste bouger les fichiers
                    mv $fichier $extension
                fi
            fi
        fi
    done 
done