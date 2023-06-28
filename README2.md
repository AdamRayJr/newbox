# newbox.sh
This bash script helps the user to export the target IP into their working environment
and create a new base directory to work in. Inside the user inputted base directory,
two other directories and three files are created. This is a simple script just to make the
initial setup of working on boxes faster and more streamlined. 

It also helps to create an alias to run the script so that the user doesn't have to type
the command everytime they start a new box. For example, instead of typing:
'/path/to/file/./newbox.sh' create an alias similar to
"alias nbox='/path/to/file/./newbox.sh'" to where all the user has to do is type 
'nbox' into the terminal. Don't forget to 'source /path/to/aliases' in your environment
and make the newbox.sh file executable.
