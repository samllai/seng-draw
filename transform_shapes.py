import sys
import copy
import math
import Line_Point_colour

#gen compilation of circles & squares here

def draw(lines, angle, it):
	new_lines = copy.deepcopy(lines)
	#scale by iteration/total iterations
	sf = 0.7
	for line in new_lines:
		line.scale(math.pow(sf, it))
		line.rotate(angle*it)
		if it%3 == 0:
			line.colour = 'Blue'
		elif it%3 == 1:
			line.colour = 'Green'
		print 'line', line

	it += 1


	
	#scale and rotate all
#	for line in new_lines:
		

#can't be constant, constant/(it+1) isn't even scale, it/total is broken

#	for k in range(it-1):
#		for line in new_lines:
#			line.scale(sf/(k+1))
#			line.rotate(angle*k)
#			print 'line', line

def load_line_file(file_object):
	line_objects = [ ]
	for line in file_object:
		# convert text line to a Line object
		line_object = line.split()
		point0 = Line_Point_colour.Point(float(line_object[1]), float(line_object[2]))
		point1 = Line_Point_colour.Point(float(line_object[3]), float(line_object[4]))
		if len(line_object) == 6:
			line_object = Line_Point_colour.Line(point0, point1, line_object[5])
		else:
			line_object = Line_Point_colour.Line(point0, point1, 'Red')

		line_objects.append(line_object)
	
	return line_objects

	#####

if len(sys.argv) != 3:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' number_of_reps rotate_angle err 1'
	sys.exit(1)
try:
	number_of_reps = int(sys.argv[1])
	rotate_angle = float(sys.argv[2])
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' number_of_reps rotate_angle'
	sys.exit(2)
if number_of_reps < 1  or number_of_reps > 7: #upper limit
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' number_of_reps'
	sys.exit(3)
if rotate_angle == 0:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' rotate_angle'
	sys.exit(4)


S = load_line_file(sys.stdin)

for i in range(number_of_reps):
	draw(S, rotate_angle, i)
