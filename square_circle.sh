
if [ $# -ne 3 ]; then
	echo "Syntax: bash square_circle radius number_of_reps rotate_angle"
	exit
fi

radius=$1
number_of_reps=$2
rotate_angle=$3

#call on new generator with radius
python generate_polygon.py 0 $radius 4 > shapes.txt
#python generate.py $radius > shapes.txt


python transform_shapes.py $number_of_reps $rotate_angle < shapes.txt > square_circle.txt
python lines_to_svg_colour.py square_circle.txt > square_circle.svg
#python lines_to_svg_colour.py shapes.txt > tester1.svg
